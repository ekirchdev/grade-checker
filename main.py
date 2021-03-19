import time
import logging
from args_parser import ArgsParser
from grade_checker import GradeChecker

# configure logging
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')
# parse args
args = ArgsParser.get_command_line_args()

logging.info(f"Started check loop. Checking every {args.interval} minutes.")

while not GradeChecker.grade_is_published(args.baseuri, args.user, args.passwd, args.module):
    time.sleep((60 * args.interval))
