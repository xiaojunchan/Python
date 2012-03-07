#!/usr/bin/env python2.5

# Copyright 2011 Karagasidis Dimitris. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice, this list of
#       conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright notice, this list
#       of conditions and the following disclaimer in the documentation and/or other materials
#       provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY KARAGASIDIS DIMITRIS ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL KARAGASIDIS DIMITRIS OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# The views and conclusions contained in the software and documentation are those of the
# authors and should not be interpreted as representing official policies, either expressed
# or implied, of Karagasidis Dimitris.

# Simple client for NoIP Dynamic DNS provider
# More info can be found here: http://www.no-ip.com/integrate/

import urllib2, re, logging, time

class NoIPClient:
  _update_url = "https://dynupdate.no-ip.com/nic/update"
  _logfile = "noipclient.log"
  _interval = 300
  _domain_name = ""
  _current_ip = ""

  def __init__( self, username, password, domain_name ):
    self._domain_name = domain_name
    password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password( None, self._update_url, username, password )
    authentication_handler = urllib2.HTTPBasicAuthHandler( password_manager )
    opener = urllib2.build_opener( authentication_handler )
    urllib2.install_opener( opener )

  def _get_url_data( self, url ):
    handler = urllib2.urlopen( url )
    data = handler.readlines()
    handler.close()
    return data

  def _check_ip( self ):
    ip_regex = "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
    worldip_data = self._get_url_data( "http://api.wipmania.com" )[0]
    ip = re.findall( ip_regex, worldip_data )
    if len( ip ) == 0:
      self._current_ip = ""
      logging.warning( "Could not resolve current ip." )
      return False
    self._current_ip = ip[0]
    logging.info( "Current ip resolved: %s" % ip[0] )
    return True

  def _update( self ):
    if self._check_ip():
      res = self._get_url_data( "%s?hostname=%s&myip=%s" % ( self._update_url, self._domain_name, self._current_ip ) )[0]
      if res.find( "good" ) != -1:
        logging.info( "DNS hostname update successful" )
      if res.find( "nochg" ) != -1:
        logging.info( "IP address is current, no update performed" )
      if res.find( "nohost" ) != -1:
        logging.error( "Hostname supplied does not exist under specified account" )
      if res.find( "badauth" ) != -1:
        logging.error( "Invalid username password combination" )
      if res.find( "badagent" ) != -1:
        logging.error( "Disabling client" )
        exit()
      if res.find( "!donator" ) != -1:
        logging.error( "An update request was sent including a feature that is not available" )
      if res.find( "abuse" ) != -1:
        logging.error( "Username is blocked due to abuse. Terminating" )
        exit()
      if res.find( "911" ) != -1:
        logging.error( "A fatal error on server side occured. Setting interval to 1800 seconds" )
        self._interval = 1800

  def _configure_logging( self ):
    logging.basicConfig(
      filename=self._logfile,
      level=logging.DEBUG,
      format="%(asctime)s\t%(levelname)s\t%(message)s",
      datefmt='%b %d %H:%M:%S'
    )

  def set_interval( self, seconds ):
    self._interval = seconds

  def set_logfile( self, filename ):
    self._logfile = filename
    self._configure_logging()

  def start( self ):
    self._configure_logging()
    while True:
      self._update()
      time.sleep( self._interval )