import smtplib
from email.message import EmailMessage
from notification_services.notification_service import NotificationService


class MailService(NotificationService):
    def __init__(self, sender, smtp_server, port, passwd, receiver):
        self._sender = sender
        self._smtp_server = smtp_server
        self._port = port
        self._passwd = passwd
        self._receiver = receiver
        super().__init__()

    def notify(self, msg_subject, msg_body):
        msg = EmailMessage()
        msg.set_content(msg_body)
        msg['Subject'] = msg_subject
        msg['From'] = self._sender
        msg['To'] = self._receiver

        try:
            server = smtplib.SMTP_SSL(self._smtp_server, self._port)
            server.login(self._sender, self._passwd)
            server.send_message(msg)
        except Exception as e:
            print(e)
        finally:
            server.quit()
