import unittest
from user_story5 import unique_family

class Family:
    def __init__(self, mar, hus_name, wifi_name):
        self.Married = mar
        self.Husband_Name = hus_name
        self.Wife_Name = wifi_name

class TestFunction(unittest.TestCase):
    def test_unique_family(self):
        fm1 = Family("1 OCT 1987", "Jonathan /Joestar/", "Joseph /Joestar/")
        fm2 = Family("1 OCT 1987", "Jonathan /Joestar/", "Joseph /Joestar/")
        fm3 = Family("1 OCT 1989", "Jonathan /Joestar/", "Joseph /Joestar/")
        fm4 = Family("1 OCT 1987", "Other", "Joseph /Joestar/")
        fm5 = Family("1 OCT 1987", "Jonathan /Joestar/", "wife")

        self.assertEqual(unique_family(fm1),"ERROR: same spouse name and marriage date has already in GEDCOM!")
        self.assertEqual(unique_family(fm2), "ERROR: same husband name and marriage date has already in GEDCOM!")
        self.assertEqual(unique_family(fm3), "ERROR: same wife name marriage date has already in GEDCOM!")
        self.assertEqual(unique_family(fm4), "ERROR: same wife name marriage date has already in GEDCOM!")
        self.assertEqual(unique_family(fm5), "ERROR: same husband name and marriage date has already in GEDCOM!")


if __name__ == "__main__":
    print('Running unit tests!')
    unittest.main()