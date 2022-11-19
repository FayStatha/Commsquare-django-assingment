import datetime


def unix_time_millis_from_datetime(dt: datetime.datetime) -> float:
    return dt.timestamp() * 1000
