from datetime import date, timedelta

from Activity import Activity
from utils import args_parser

daily_date = date.today() if args_parser.get_parser().parse_args().start_date is None else args_parser.get_parser().parse_args().start_date

Activity(daily_date).render()