from datetime import date

from .Activity import Activity
from .utils import args_parser
from .utils import conf_manager

token = conf_manager.get_token()
daily_date = date.today() if args_parser.get_parser().parse_args().start_date is None else args_parser.get_parser().parse_args().start_date

Activity(token, daily_date).render()