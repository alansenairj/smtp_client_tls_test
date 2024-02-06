import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 587
smtp_server = "smtprelay.unimedbh.com.br"
login = "smtp.app.company.hml" 
password = "password"

sender_email = "test@example.com"
receiver_email = "test@mydomain.com.br"
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

text = """\
Teste email em python"""

html = """\
<html>
  <body>
    <p>Hi,<br>
       o email está chegando:</p>
    <p><a href="teste">SMTP Server for Testing: Cloud-based or Local?</a></p>
    <p> Feel free to <strong>let us</strong> know what content would be useful for you!</p>
  </body>
</html>
"""

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()  # Upgrade the connection to a secure TLS connection
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Sent')
