import logging
from notification_services.mail_service import MailService
from notification_services.stdout_service import StdoutService


class MailServiceFactory(object):
    @staticmethod
    def _verify_args(args):
        if not args.smtp_passwd:
            raise ValueError("You did not configure a value for parameter 'smtp_passwd'!")
        elif not args.smtp_port:
            raise ValueError("You did not configure a value for parameter 'smtp_port'!")
        elif not args.smtp_server:
            raise ValueError("You did not configure a value for parameter 'smtp_server'!")
        elif not args.receiver:
            raise ValueError("You did not configure a value for parameter 'receiver'!")
        elif not args.sender:
            raise ValueError("You did not configure a value for parameter 'sender'!")

    @staticmethod
    def from_args(args):
        # if all args for sending mails are None, the user probably does not want to send mails
        # use StdoutService instead
        if not args.smtp_passwd and not args.smtp_port \
                and not args.smtp_server and not args.sender and not args.receiver:
            logging.warning("You configured none of the properties to send e-mails. Using StdoutService instead.")
            return StdoutService()
        # verify all properties are configured
        MailServiceFactory._verify_args(args)
        return MailService(sender=args.sender,
                           smtp_server=args.smtp_server,
                           port=args.smtp_port,
                           passwd=args.smtp_passwd,
                           receiver=args.receiver)
