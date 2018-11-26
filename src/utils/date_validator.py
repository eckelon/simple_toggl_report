from datetime import datetime


def valid_date_type(arg_date_str):
    if arg_date_str is None:
        return None
    try:
        return datetime.strptime(arg_date_str, "%Y-%m-%d")
    except ValueError:
        msg = "Given Date ({0}) not valid! Expected format, YYYY-MM-DD!".format(arg_date_str)
        raise msg
