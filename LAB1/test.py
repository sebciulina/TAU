import unittest
from main import quicksort


class TestQuicksort(unittest.TestCase):

    def test_sort_empty_list(self):
        self.assertEqual(quicksort([]), [])

    def test_sort_single_element_list(self):
        self.assertEqual(quicksort([5]), [5])

    def test_sort_already_sorted_list(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted_list(self):
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_sort_list_with_duplicate_elements(self):
        self.assertEqual(quicksort([2, 5, 3, 2, 1, 5, 4]), [1, 2, 2, 3, 4, 5, 5])

    def test_sort_list_with_negative_elements(self):
        self.assertEqual(quicksort([-5, 2, 0, -3, 7]), [-5, -3, 0, 2, 7])

    def test_sort_list_with_identical_values(self):
        arr = [4, 4, 4, 4, 4, 4]
        self.assertEqual(quicksort(arr), [4, 4, 4, 4, 4, 4])

    def test_sort_list_with_decimals(self):
        self.assertEqual(quicksort([2.4, 1.2, 3.6, 2.1, 0.5]), [0.5, 1.2, 2.1, 2.4, 3.6])

    def test_sort_list_with_strings(self):
        self.assertEqual(quicksort(['b', 'a', 'c', 'e', 'd']), ['a', 'b', 'c', 'd', 'e'])

    def test_sort_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            quicksort([1, 'a', 2.5, True])


if __name__ == '__main__':
    unittest.main()
