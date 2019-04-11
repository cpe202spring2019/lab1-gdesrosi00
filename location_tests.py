import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):    #tests the repr function and the string it produces
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_eq(self):    #tests the eq method to see if identical locations are equal
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("Lakeside", 1, 2)
        self.assertEqual(loc1, loc2)
        self.assertFalse(loc1 == loc3)
       
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
