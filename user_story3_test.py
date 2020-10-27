import unittest
import datetime
from user_story3 import born_within30

class test_check_born_within30(unittest.TestCase):

    def test_check_born_within30(self):

        date_now = datetime.datetime(2020, 10, 26, 1, 0, 0)
        date1 = datetime.datetime(2020, 10, 15, 0, 0, 0)
        date2 = datetime.datetime(2020, 9, 14, 0, 0, 0)
        date3 = datetime.datetime(2020, 9, 28, 0, 0, 0)
        date4 = datetime.datetime(1991, 8, 15, 0, 0, 0)
        date5 = datetime.datetime(2020, 11, 16, 0, 0, 0)
        date6 = datetime.datetime(2020, 11, 1, 0, 0, 0)
        date7 = datetime.datetime(2020, 12, 17, 0, 0, 0)
        date8 = datetime.datetime(2020, 11, 28, 0, 0, 0)

        self.assertEqual(born_within30(date1, date_now, 'Hu'), 'Hu were born within 11 days')
        self.assertEqual(born_within30(date2, date_now, 'Goe'), None)
        self.assertEqual(born_within30(date3, date_now, 'Tom'), 'Tom were born within 28 days')
        self.assertEqual(born_within30(date4, date_now, 'Amy'), None)
        self.assertEqual(born_within30(date5, date_now, 'Jack'), 'Jack were born within 20 days')
        self.assertEqual(born_within30(date6, date_now, 'Mike'), 'Mike were born within 5 days')
        self.assertEqual(born_within30(date7, date_now, 'Dan'), None)
        self.assertEqual(born_within30(date8, date_now, 'Emily'), None)

if __name__ == '__main__':
    print('Running Unittest!')
    unittest.main()
