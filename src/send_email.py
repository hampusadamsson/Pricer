import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(username, password, custom_message, date):
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = username
    msg['Subject'] = "Price checker"
    
    msg.attach(MIMEText('''<!DOCTYPE html>
    <html>
    <head>
    <title>Price checker</title>
    </head>
    <body>
    </head>
    <body>    
    <h2>Price checker</h2>
    <h3>{0}</h3>
    <table>
    <tr>
    <th>Price</th>
    <th>Company</th>
    </tr>
    {1}
    </table>

    <p><img src="cid:0"></p>
    </body></html>'''.format(date, custom_message), 'html', 'utf-8'))

    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.set_debuglevel(1)
        server.login(username, password)
        server.sendmail(username, [username], msg.as_string())