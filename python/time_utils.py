from datetime import datetime
import time
from typing import Union

import pytz # pylint: disable=import-error

time_zones_builtin = {
    "pdt": pytz.timezone("America/Los_Angeles")
}

def utc_str_to_utc_dt(dt_str_utc: str) -> datetime:
    """Convert a UTC timestring to datetime

    Args:
        dt_str_utc: timestring of form "2019-11-08T15:51:40" or
            "2019-11-08 15:51:40"
    
    Returns:
        the datetime
    """
    dt_str_utc = dt_str_utc.strip().replace(' ', 'T')
    dt_str_utc = dt_str_utc.strip().replace('Z', '')
    try:
        dt_utc = datetime.strptime(dt_str_utc, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        dt_utc = datetime.strptime(dt_str_utc, "%Y-%m-%dT%H:%M:%S")
    return dt_utc

def local_str_to_utc_dt(
        dt_str_local: str,
        local_tz: Union[str, pytz.timezone] = 'pdt') -> datetime:
    """Convert a local timestring to datetime

    Args:
        dt_str_utc: timestring of form "2019-11-08T15:51:40" or
            "2019-11-08 15:51:40"
        local_tz: the local timezone for dt_str_local. If a string, should be a
            key in time_zones_builtin, and will be used to look up a pytz.timezone
    
    Returns:
        the datetime
    """
    if isinstance(local_tz, str):
        local_tz = time_zones_builtin[local_tz.lower()]
    dt_str_local = dt_str_local.replace(' ', 'T')
    dt_str_local = dt_str_local.strip().replace('Z', '')
    try:
        dt_local = datetime.strptime(dt_str_local, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        dt_local = datetime.strptime(dt_str_local, "%Y-%m-%dT%H:%M:%S")
    dt_local = local_tz.localize(dt_local, is_dst=None)
    return dt_local.astimezone(pytz.utc)

def isoformat_strict(dt: datetime) -> str:
    """Get an isoformat string for dt that always has microseconds

    Regular isoformat() will drop the microseconds from the string if they're 0
    
    Args:
        dt: the datetime
    
    Returns:
        the string representation
    """
    if dt.microsecond == 0:
        return dt.isoformat() + '.000000'
    return dt.isoformat()