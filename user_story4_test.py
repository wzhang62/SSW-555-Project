import unittest,datetime
from user_story4 import old_father,old_mother

class TestMethod(unittest.TestCase):
    def test_father_not_old(self):
        date1 = datetime.datetime(1970,3,24,0,0,0)
        date2 = datetime.datetime(1930,4,4,0,0,0)
        date3 = datetime.datetime(2002,3,29,0,0,0)
        self.assertFalse(old_father(date1,date3))
        self.assertTrue(old_father(date2,date3))

    def test_mother_not_old(self):
        date1 = datetime.datetime(1977,1,29,0,0,0)
        date2 = datetime.datetime(1903,4,12,0,0,0)
        date3 = datetime.datetime(1983,7,7,0,0,0)
        self.assertFalse(old_mother(date1,date3))
        self.assertTrue(old_mother(date2,date3))

if __name__ == "__main__":
    print('Running unit tests')
    unittest.main()
