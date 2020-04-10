#!/usr/bin/python3

# email with attachments and smtplib example

import email
import smtplib
import sys

from email.mime.text import MIMEText

# email
msg = email.message.EmailMessage()
msg['Subject'] = 'my subject'
msg['From'] = 'email@my.domain'
msg['To'] = 'recipient@their.domain'
msg.attach(MIMEText('my message', 'plain'))
with open('/tmp/test.pdf', 'rb') as fd:
    pdf_data = fd.read()
    msg.add_attachment(pdf_data, maintype='application', subtype='pdf', filename='test.pdf')
with open('/tmp/test.txt', 'rb') as fd:
    txt_data = fd.read()
    msg.add_attachment(txt_data, maintype='text', subtype='plain', filename='test.txt')

# smtplib
try:
    s = smtplib.SMTP('smtp.my.domain')
    s.send_message(msg)
    s.quit()
except smtplib.SMTPException as e:
    print(e)
    sys.exit(1)
