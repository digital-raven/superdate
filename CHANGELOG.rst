===========
 Changelog
===========
All notable changes will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

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
