import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        self.assertEqual(max_list_iter([0, 1, 3, 2]), 3) #tests max_list_iter with a regular list
        self.assertEqual(max_list_iter([]), None)        #tests max_list_iter with an empty list
        self.assertEqual(max_list_iter([1, 1, 1]), 1)    #tests max_list_iter with a list of the same number
        tlist = None
        with self.assertRaises(ValueError):              # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])   #tests reverse_rec with a regular list
        self.assertEqual(reverse_rec([]), [])            #tests reverse_rec with an empty list
        emptylist = None
        with self.assertRaises(ValueError):              #checks to make sure a ValueError is raised when a nonetype object is passed into the function
            reverse_rec(emptylist)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )       #tests bin_search with a normal list and target
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0 )       #tests bin_search with the lower end point of the list as the target 
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8 )      #tests bin_search with the higher end point of the list as the target
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None )    #tests bin_search with a target that is not in the list
        list_none = None
        with self.assertRaises(ValueError):    #checks to make sure a ValueError is raised when the list is none
             bin_search(1, 0, 9, list_none)

if __name__ == "__main__":
        unittest.main()
