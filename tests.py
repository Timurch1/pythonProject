from main import ilya_solution
import unittest


class TestStringMethods(unittest.TestCase):
    def test_find_longest_substring_first(self):
        self.assertEqual(ilya_solution("aacifgadddddd"), "cifgad")

    def test_find_longest_substring_second(self):
        self.assertEqual(ilya_solution("dddd"), "d")

    def test_find_longest_substring_third(self):
        self.assertEqual(ilya_solution("abcabad"), "abc")


if __name__ == '__main__':
    unittest.main()
