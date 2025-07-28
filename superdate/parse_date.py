from datetime import date, datetime, timedelta

import parsedatetime as pdt


def parse_date(date_, extra_formats=None, force_time=False, _cache={}):
    """ Parse a str into a date or datetime.

    This function will first try to parse isoformat (datetime.fromisoformat)
    If that fails then it tries other formats before parsing from plain
    english.

    - isoformat
    - some pre-defined common formats
    - plain english

    If a time is parsed from english then it can have precision down
    to the second.

    Args:
        date_: Date to parse.
        extra_formats: List of extra date formats to consider.
        force_time: parse_date will return a date object (no time) if no
            time components were parsed. This option forces a datetime object
            to be returned.

        _cache: Do not touch. This caches requests and will clear if
            a new second has ticked over since the previous call.

    Returns:
        A date or datetime object.

    Raises:
        ValueError if date_ could not be parsed.
    """
    if type(date_) in [date, datetime]:
        if force_time and type(date_) is date:
            date_ = datetime(date_.year, date_.month, date_.day)
        return date_

    date_ = str(date_)

    # Init cache. It clears if the second has changed since the previous call.
    now = datetime.now()
    now = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)

    if '__init' not in _cache or now != _cache['__init']:
        _cache.clear()
        _cache['__init'] = now
        _cache[True] = {}
        _cache[False] = {}

    if date_ in _cache[force_time]:
        return _cache[force_time][date_]

    # Easy mode try: From ISO
    try:
        d = datetime.fromisoformat(date_)
        if not force_time and (d.hour, d.minute, d.second, d.microsecond) == (0, 0, 0, 0):
            d = d.date()

        return d
    except ValueError:
        pass

    # Try some other common formats
    extra_formats = extra_formats or []
    datefmts = extra_formats + [
        '%Y/%m/%d',
        '%m/%d/%Y',
        '%d/%m/%Y',
        '%d-%m-%Y',
        '%Y-%m-%d, %a',
        '%Y-%m-%d, %a, %H:%M',
    ]

    for fmt in datefmts:
        try:
            d = datetime.strptime(date_, fmt)
            if not force_time and (d.hour, d.minute, d.second, d.microsecond) == (0, 0, 0, 0):
                d = d.date()
            _cache[force_time][date_] = d
            return d

        except ValueError:
            pass

    # No matches. Expensive general parser.
    cal = pdt.Calendar(version=pdt.VERSION_CONTEXT_STYLE)
    d, ctx = cal.parse(date_)

    if not ctx.hasDateOrTime:
        raise ValueError(f'The date "{date_}" could not be parsed.')

    if not ctx.hasTime and not force_time:
        _cache[force_time][date_] = date(*d[:3])
    else:
        _cache[force_time][date_] = datetime(*d[:6])

    return _cache[force_time][date_]
