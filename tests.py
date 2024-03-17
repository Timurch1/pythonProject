from main import find_longest_substring
import unittest


class TestStringMethods(unittest.TestCase):
    def test_find_longest_substring_first(self):
        self.assertEqual(find_longest_substring("abcifghadddddd"), "abcifgh")

    def test_find_longest_substring_second(self):
        self.assertEqual(find_longest_substring("dddd"), "d")

    def test_find_longest_substring_third(self):
        self.assertEqual(find_longest_substring("abcabad"), "abcifgh")


if __name__ == '__main__':
    unittest.main()
