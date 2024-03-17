from main import ilya_solution
import unittest


class TestStringMethods(unittest.TestCase):
    def test_find_longest_substring_first(self):
        self.assertEqual(ilya_solution("aacifgadddddd"), "cifgad")

    def test_find_longest_substring_second(self):
        self.assertEqual(ilya_solution("dddd"), "d")

    def test_find_longest_substring_third(self):
        self.assertEqual(ilya_solution("abcabad"), "abc")

    def test_roman_to_int_first(self):
        self.assertEqual(ilya_solution("III"), 3)

    def test_roman_to_int_second(self):
        self.assertEqual(ilya_solution("LVIII"), 58)

    def test_roman_to_int_third(self):
        self.assertEqual(ilya_solution("MCMXCIV"), 1994)


if __name__ == '__main__':
    unittest.main()
