import unittest
from datetime import date, datetime

from superdate import parse_date
from superdate import SuperDate as SD


class TestParseDate(unittest.TestCase):
    def test_basic_init(self):
        """ Test basic initializer behaviors
        """
        s = SD('today')
        o = SD(s, force_time=True)

        self.assertIs(type(s._date), date)
        self.assertIs(type(o._date), datetime)

        self.assertEqual(datetime.now().date(), s._date)

        now = datetime.now()
        now = datetime(now.year, now.month, now.day)
        self.assertEqual(now, o._date)

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
        self.assertEqual(SD('today'), SD('today'))
        self.assertEqual(SD('today'), SD('now'))
        self.assertEqual(SD('now'), SD('today'))
        self.assertEqual(SD('now'), SD('now'))

    def test_second_parsing(self):
        d = SD('30 seconds from today at noon')
        exp = datetime.now()
        exp = datetime(exp.year, exp.month, exp.day, 12, 0, 30)
        self.assertEqual(exp, d._date)

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

        if SD('now') < SD('noon'):
            self.assertTrue(SD('Wednesday', force_time=True) < 'Wednesday at noon')
        else:
            self.assertFalse(SD('Wednesday', force_time=True) < 'Wednesday at noon')

        # Time should be lopped off because 'Wednesday' has no time.
        self.assertFalse(SD('Wednesday at noon') < 'Wednesday')

        # GT
        self.assertTrue(SD('today') > 'yesterday')


if __name__ == '__main__':
    unittest.main()
