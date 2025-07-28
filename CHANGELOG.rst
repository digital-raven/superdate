===========
 Changelog
===========
All notable changes will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[unreleased]
============

Fixed
-----
- Unit tests passing or failing depending on what time of day they were run.

[0.2.1] - 2023-03-01
====================

Fixed
-----
- Less restrictive python3 and parsedatetime version requirement.

[0.2.0] - 2023-03-01
====================

Removed python3-dateutil. It was causing inconsistent parsing in examples
like...

::

     # Lets say today is Wednesday, March first at 8am
     parse_date('wednesday') #  => March 1. Handled by dateutil
     parse_date('wednesday at noon') #  => March 8. Handled by pdt

This does mean that dates like "Wedesday" or "January" will default to
"Next Wednesday" or "Next January" if those relative dates have already
passed.

But Parsedate time handles more cases than dateutil, and consistent behavior
contributes great to intuitive behavior than mixing parsers.

Added
-----
- SuperDate now accepts extra formats.
- English requests can be parsed down to the second. Handles cases for
  "alarm clock" apps where seconds matter.

Changed
-------
- Cache now clears every second and ISO parses aren't cached. This is to
  handle cases where a lot of dates are parsed with microseconds. These are
  likely to be scientific datasets, and will likely be stored in ISO format
  which parses quickly without a cache and caching those results would
  simultaneously thrash and eat tons of memory.

Fixed
-----
- SuperDate handles force_time correctly.
- More robust unit tests.

Removed
-------
- python3-dateutil dependency.

[0.1.2] - 2023-02-26
====================
Performance bugfix.

Fixed
-----
- Proper cache checking.

[0.1.1] - 2023-02-26
====================
Initial release of superdate. This includes the parse_date function and
SuperDate class.

The parse_date function returns a date or datetime object parsed from
a string. The SuperDate class overloads comparison operators so the
date object can be compared against strings and other dates / datetimes.
It also forwards all dot operators to the underlying date / datetime
object so it should be usable anywhere a standard date or datetime is used.

Added
-----
- SuperDate class. This class can act identically to date or datetime
  while being able to be initialized from plain english strings.
- parse_date function to return raw date or datetime parsed from a string.
