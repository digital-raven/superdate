from datetime import date, datetime

from superdate.parse_date import parse_date


class SuperDate:
    """ Date class for super easy parsing and comparison.

    Comparison operators are overloaded so if a date is compared with a
    time then the time element will be omitted.

    This means comparisons like

        SuperDate('wednesday at noon') < 'Wednesday at 4pm'

    Will evaluate to True, but

        SuperDate('wednesday') < 'Wednesday at 4pm'

    will return False. This is because a user asking if a time is less than
    "Wednesday" is probably looking to omit all events on Wednesday.

    If time elements are always desired, then pass the force_time flag.

    Additionally, all dot calls to this class are forwarded to the underlying
    date or datetime object. This should produce an identical interface to
    python3's standard date / datetime objects.
    """
    def __init__(self, date_, force_time=False):
        """ date needs to be parseable according to parse_date

        Args:
            date_: Date to parse
            force_time: Force a time element when parsing from a string.

        Raises:
            ValueError if the date could not be parsed.
        """
        if type(date_) is SuperDate:
            self.__dict__['_date'] = date_._date
        else:
            self.__dict__['_date'] = parse_date(date_, force_time)

    def __getattr__(self, key):
        """ If not referring to any SuperDate attrs then forward to date.
        """
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            return self._date.__getattribute__(key)

    def __setattr__(self, key, value):
        """ This should always raise because datetimes are immutable.
        """
        raise AttributeError('date and datetime objects are immutable')

    def __str__(self):
        return str(self._date)

    def __hash__(self):
        return hash(self._date)

    def _compato(self, o):
        """ Return type-compatible versions of self._date and o

        If the types mismatch (datetime / date) then the datetime will be
        tied down to its date elements.
        """
        if type(o) is SuperDate:
            o = o._date
        else:
            o = parse_date(o)

        st = type(self._date)
        ot = type(o)

        if st is ot:
            return self._date, o

        # tie down datetimes to dates
        elif st is datetime and ot is date:
            return self._date.date(), o

        return self._date, o.date()

    def __lt__(self, o):
        s, o = self._compato(o)
        return s < o

    def __gt__(self, o):
        s, o = self._compato(o)
        return s > o

    def __ge__(self, o):
        s, o = self._compato(o)
        return s >= o

    def __le__(self, o):
        s, o = self._compato(o)
        return s <= o

    def __eq__(self, o):
        if o is None:
            return False

        s, o = self._compato(o)
        return s == o

    def __ne__(self, o):
        if o is None:
            return True

        s, o = self._compato(o)
        return s != o

    def __sub__(self, o):
        s, o = self._compato(o)
        return s - o

    def __add__(self, o):
        s, o = self._compato(o)
        return s + o
