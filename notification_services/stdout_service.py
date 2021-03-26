from notification_services.notification_service import NotificationService
import logging


class StdoutService(NotificationService):
    def notify(self, msg_subject, msg_body):
        logging.info("[%s] %s" % (msg_subject, msg_body))
