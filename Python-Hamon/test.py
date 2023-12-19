import unittest
from exersise1 import palindrome,freq


class TestforPalindrome(unittest.TestCase):
    
    def test_is_palindrome(self):
        string="nivin"
        self.assertTrue(palindrome(string))


    def test_is_not_palindrome(self):
        string="egg"
        self.assertFalse(palindrome(string))

    def test_empty(self):
        string=""
        self.assertTrue(palindrome(string))


class TestforFreq(unittest.TestCase):
    def test_dict(self):
        expected_dict={'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
        string="hello world"
        self.assertDictEqual(expected_dict,freq(string))
        



   












     











if __name__ == '__main__':
    unittest.main()