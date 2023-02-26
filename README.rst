===========
 superdate
===========
SuperDate: A super easy to use date parsing library.

Building and installation
=========================
Available from PyPi; Just ``pip3 install superdate``

Alternatively, clone this repo and then pip3 install.

::

    pip3 install .

Usage 
=====
superdate contains two main components; the parse_date function and
SuperDate class.

The parse_date function allows for super intuitve date parsing, while
the SuperDate class overloads comparison operators to allow for intuitive
date comparisions against strings or date / datetime objects.

parse_date
----------
The parse_date function parses dates from strings. These can be
plain iso strings or coloquial enslish strings. Plain english strings
are parsed with down to minute precision.

If a time was detected, then a datetime will be returned. If no time
information was detected then a date object will be returned. A
datetime can be forced to return with ``force_time=True``.

::

    # Some examples. Logged on Febuary 26th 2023.

    >>> from superdate import parse_date

    >>> parse_date('1970-1-1')
    datetime.date(1970, 1, 1)

    >>> parse_date('today')
    datetime.date(2023, 2, 26)

    # Force a time
    >>> parse_date('today', force_time=True)
    datetime.datetime(2023, 2, 26, 9, 0)

    >>> parse_date('now')
    datetime.datetime(2023, 2, 26, 14, 32)

    >>> parse_date('saturday')
    datetime.date(2023, 3, 4)

    >>> parse_date('saturday at noon')
    datetime.datetime(2023, 3, 4, 12, 0)

    >>> parse_date('January')
    datetime.date(2023, 1, 26)

    >>> parse_date('January next year')
    datetime.date(2024, 1, 1)


SuperDate
---------
The SuperDate class wraps the parse_date function, but overloads all
comparison operators to allow for more intuitive plain-english comparisons.

Comparisons between dates and datetimes will ignore the time. This is
because a very common use case is, for example, a user who asks "what
appointments are on wednesday?"

::

    [a for a in appointments if a.date == 'Wednesday']

Typically "Wednesday" would include hour 0, minute 0, and second 0, which
isn't technically equivalent to an appointment at 4pm. Obviously this user
wants to see all their appointments on Wednesday, so the time for each
appointment will be ignored when comparing against a plain date.

::

    # Some examples
    from superdate import SuperDate

    SuperDate('Wednesday') == 'Wednesday'  # => True
    SuperDate('Wednesday') < 'Wednesday 4pm'  # => False
    SuperDate('Wednesday') == 'Wednesday 4pm'  # => True
    SuperDate('Wednesday at noon') < 'Wednesday 4pm'  # => True

    # Will evaluate to True because we forced a time.
    SuperDate('Wednesday', force_time=True) < 'Wednesday 4pm'  # => True

All dot operators (.hour .day .strftime etc...) are forwarded to the
underlying python3 standard date / datetime ojbect, so this class should
be usable anywhere a regular datetime is.

Maintenance and versioning
==========================
Update the CHANGELOG when and version in pyproject.toml when cutting a release.

Build with ``python3 -m build`` and use ``twine upload -r pypi dist/*`` to
upload to pypi.
