import argparse
import config as cfg
import validators


class ArgsParser(object):
    @staticmethod
    def get_command_line_args():
        """
        Parse arguments from command line.
        :return: Parsed command line arguments.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('--module', '-m', type=str,
                            help='Module to check.',
                            required=True)
        parser.add_argument('--user', '-u', type=str,
                            help='Username for login.',
                            required=True)
        parser.add_argument('--passwd', '-p', type=str,
                            help='Password for login.',
                            required=True)
        parser.add_argument('--interval', '-i', type=int,
                            help='Determine how often the check should be executed. Set a value of <X> to execute the '
                                 'check every <X> minutes. Default: %d' % cfg.INTERVAL, default=cfg.INTERVAL)
        parser.add_argument('--baseuri', '-b', type=str,
                            help='The url of your grade management system. Default: %s' % cfg.WEBSITE_URI,
                            default=cfg.WEBSITE_URI)
        args = parser.parse_args()

        if not validators.url(args.baseuri):
            raise ValueError("Given value for baseuri is not valid: %s" % args.baseuri)
        if not validators.between(args.interval, 1, 10.080):
            raise ValueError("Invalid interval value: %s" % str(args.interval))

        return args
