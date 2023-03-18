import unittest
from datetime import date, datetime

from superdate import parse_date
from superdate import SuperDate as SD


class TestParseDate(unittest.TestCase):

    def test_basic_date_parsing(self):
        """ Make sure the underlying data is a date.
        """
        act = SD('today')
        exp = parse_date('today')
        self.assertEqual(exp, act._date)

    def test_is_date(self):
        """ Something with no time elements should result in 'date' type
        """
        act = SD('today')
        self.assertTrue(type(act._date) is date)

    def test_is_datetime(self):
        """ Something with time elements should result in 'datetime' type
        """
        act = SD('now')
        self.assertTrue(type(act._date) is datetime)

    def test_str_equivalence(self):
        """ Output as str should equal actual date.
        """
        exp = SD('today')
        act = SD(str(exp))
        self.assertEqual(exp, act)

    def test_super_date_comparison(self):
        """ Test comparison between two SuperDates
        """
        d1 = SD('today')
        d2 = SD('today')
        self.assertEqual(d1, d2)
        self.assertEqual(d1._date, d2._date)

    def test_string_comparisons(self):
        """ Test a whole bunch of comparisons.
        """
        # EQ
        self.assertEqual(SD('today'), 'now')
        self.assertEqual(SD('today'), 'today at noon')
        self.assertEqual(SD('Wednesday'), 'Wednesday at 4pm')
        self.assertEqual(SD('Wednesday'), 'Wednesday at 1am')

        # LT
        self.assertTrue(SD('yesterday') < 'today')
        self.assertTrue(SD('Wednesday at noon') < 'Wednesday at 4pm')

        self.assertFalse(SD('Wednesday') < 'Wednesday at noon')
        self.assertTrue(SD('Wednesday', force_time=True) < 'Wednesday at noon')
        self.assertFalse(SD('Wednesday at noon') < 'Wednesday')

        # GT
        self.assertTrue(SD('today') > 'yesterday')


if __name__ == '__main__':
    unittest.main()
