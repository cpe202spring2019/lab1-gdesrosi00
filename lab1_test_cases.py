import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        self.assertEqual(max_list_iter([0, 1, 3, 2]), 3)
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([1, 1, 1]), 1)
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([]), [])
        emptylist = None
        with self.assertRaises(ValueError):
            reverse_rec(emptylist)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8 )
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None )
        list_none = None
        with self.assertRaises(ValueError):
             bin_search(1, 0, 9, list_none)

if __name__ == "__main__":
        unittest.main()
