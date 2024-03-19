from main import ilya_solution, search_insert_position
import unittest


class TestStringMethods(unittest.TestCase):
    def test_find_longest_substring_first(self):
        self.assertEqual(ilya_solution("aacifgadddddd"), "cifgad")

    def test_find_longest_substring_second(self):
        self.assertEqual(ilya_solution("dddd"), "d")

    def test_find_longest_substring_third(self):
        self.assertEqual(ilya_solution("abcabad"), "abc")

    def test_search_insert_position_first(self):
        self.assertEqual(search_insert_position([1, 3, 5, 7], 3), 1)

    def test_search_insert_position_second(self):
        self.assertEqual(search_insert_position([1, 3, 5, 7], 4), 2)

    def test_search_insert_position_third(self):
        self.assertEqual(search_insert_position([1, 3, 5, 7], 12), 4)


if __name__ == '__main__':
    unittest.main()
