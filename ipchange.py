#!/usr/bin/env python
# encoding: utf-8
"""
Script to email IP whenever it changes. Also updates DynDns hostname.
Version 1.0
 
Created by Kunal Dua on 2010-05-10
http://www.kunaldua.com/blog/?p=360
 
This program is free software; you may redistribute it and/or
modify it under the same terms as Python itself.
"""
 
def send_mail(subject, content):
        import smtplib
        from email.mime.text import MIMEText
        SERVER = "mail.hku.hk"
        PORT = 25 #Use 25 if this doesn't work
        FROM = "MAGI <yanyan07@hku.hk>"
        TO = "yanyan.ryan.leung@gmail.com"
 
        SUBJECT = "[MAGI]"+ subject
        TEXT = content
 
        message = MIMEText(TEXT)
        message['Subject'] = SUBJECT
        message['From'] = FROM
        message['To'] = TO
 
        server = smtplib.SMTP(SERVER, PORT)
        server.sendmail(FROM, TO, message.as_string())
        server.quit()
 
if __name__ == '__main__':
	import os
	import socket
	s = socket.socket(socket.AF_INET)
	s.connect(("gmail.com",80))
	ipin = str(s.getsockname())
	ipex = os.popen("curl icanhazip.com").read()
	send_mail("IP update: " + ipin, "internal:\n" + ipin + "\nexternal:\n" + ipex)
