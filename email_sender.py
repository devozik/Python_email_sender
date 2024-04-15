import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'your name'
email['to'] = 'to who'
email['subject'] = 'title'

email.set_content(html.substitute(name='name'), 'html')

#
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('user@mail.com', 'randompassword')
    smtp.send_message(email)
    print('e-mail sent!')