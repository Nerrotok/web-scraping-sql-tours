import smtplib
import ssl
import config


def send_email(message):
    host = config.host
    port = config.port
    username = config.user_name
    password = config.password
    receiver = config.receiver
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
