import argparse
from .date_validator import valid_date_type

parser = argparse.ArgumentParser(description='Date validator')
parser.add_argument('-d', '--daily-date',
                    dest='start_date',
                    type=valid_date_type,
                    default=None,
                    required=False,
                    help='start date in format "YYYY-MM-DD"')


def get_parser():
    return parser
