import unittest
from datetime import date, datetime

from superdate.parse_date import parse_date
from superdate.SuperDate import SuperDate


class TestParseDate(unittest.TestCase):

    def test_basic_date_parsing(self):
        """ Make sure the underlying data is a date.
        """
        act = SuperDate('today')
        exp = parse_date('today')
        self.assertEqual(exp, act._date)

    def test_is_date(self):
        """ Something with no time elements should result in 'date' type
        """
        act = SuperDate('today')
        self.assertTrue(type(act._date) is date)

    def test_is_datetime(self):
        """ Something with time elements should result in 'datetime' type
        """
        act = SuperDate('now')
        self.assertTrue(type(act._date) is datetime)

    def test_str_equivalence(self):
        """ Output as str should equal actual date.
        """
        exp = SuperDate('today')
        act = SuperDate(str(exp))
        self.assertEqual(exp, act)

    def test_comparison(self):
        """ Test comparison between two SuperDates
        """
        d1 = SuperDate('today')
        d2 = SuperDate('today')
        self.assertEqual(d1, d2)
        self.assertEqual(d1._date, d2._date)

    def test_comparison_with_time(self):
        """ Test comparison between two SuperDates, but one has a time.
        """
        d1 = SuperDate('today')
        d2 = SuperDate('now')
        self.assertEqual(d1, d2)

    def test_lt(self):
        """ Test < operator.
        """
        l_ = SuperDate('yesterday')
        r = SuperDate('today')
        self.assertTrue(l_ < r)

        l_ = SuperDate('Wednesday')
        r = SuperDate('Wednesday at noon')
        self.assertFalse(l_ < r)

        l_ = SuperDate('Wednesday at noon')
        r = SuperDate('Wednesday at 4pm')
        self.assertTrue(l_ < r)

        l_ = SuperDate('Wednesday at noon')
        r = SuperDate('Wednesday')
        self.assertFalse(l_ < r)

    def test_gt(self):
        """ Test > operator.
        """
        l_ = SuperDate('yesterday')
        r = SuperDate('today')
        self.assertTrue(r > l_)

        # with time
        r = SuperDate('now')
        self.assertTrue(r > l_)


if __name__ == '__main__':
    unittest.main()
