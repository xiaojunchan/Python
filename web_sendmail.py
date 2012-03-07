import smtplib
import sys

SERVER = "mail.hku.hk"
sender = "yanyan07@hku.hk"
receivers = ["yanyan_leung@hotmail.com"] # must be a list
sendername = "MAGI"
subject = "[Notice from MAGI]"
text = string.join(sys.argv[1:])

message = """\
From: %s %s %s %s
To: %s
Subject: %s

%s
""" % (sendername, " <", sender, "> ", ", ".join(receivers), subject, text)

# Send the mail

try:
   smtpObj = smtplib.SMTP(SERVER)
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"