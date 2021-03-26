import time
import logging
from args_parser import ArgsParser
from grade_checker import GradeChecker
from notification_services.mail_service_factory import MailServiceFactory

# configure logging
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')
# parse args
args = ArgsParser.get_command_line_args()
service = MailServiceFactory.from_args(args)

logging.info(f"Started check loop. Checking every {args.interval} minutes.")

while not GradeChecker.grade_is_published(website_url=args.baseuri,
                                          user=args.user,
                                          passwd=args.passwd,
                                          module_name=args.module,
                                          browser=args.browser,
                                          notification_service=service):
    time.sleep((60 * args.interval))
