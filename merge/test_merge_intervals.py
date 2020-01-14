import unittest
from .merge_intervals import merge_overlapping_intervals


class TestOverlappingIntervals(unittest.TestCase):

    def test_one(self):
        input_array = [[22,30], [2,19], [14, 23], [40,80]]
        output_array =  [[2,30], [40,80]]
        self.assertEqual(merge_overlapping_intervals(input_array),
                        output_array)
    
    def test_two(self):
        input_array = [[2,3], [2,19], [34, 53], [4,8]]
        output_array =  [[2, 19], [34, 53]]
        self.assertEqual(merge_overlapping_intervals(input_array),
                        output_array)
    
    def test_three(self):
        input_array = [[15,30], [14, 23], [4,8]]
        output_array =  [[4,8], [14, 30]]
        self.assertEqual(merge_overlapping_intervals(input_array),
                        output_array)
    
    def test_four(self):
        input_array = [[1, 3], [45,70], [4, 21], [2,19], [14, 23], [4,8]]
        output_array =  [[1,23], [45,70]]
        self.assertEqual(merge_overlapping_intervals(input_array),
                        output_array)