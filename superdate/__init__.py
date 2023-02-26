import sys

if sys.version_info >= (3, 8):
    from importlib import metadata
else:
    import importlib_metadata as metadata

__version__ = metadata.version('superdate')

from superdate.parse_date import parse_date
from superdate.SuperDate import SuperDate
