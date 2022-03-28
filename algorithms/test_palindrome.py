from unittest import TestCase
from palindrome import Palindrome


class TestPalindrome(TestCase):
    def test_palindromes(self):
        self.assertTrue(Palindrome("abba").isPalindrome)  # add assertion here
        self.assertTrue(Palindrome("abxba").isPalindrome)  # add assertion here
        self.assertTrue(Palindrome("xyzzyx").isPalindrome)  # add assertion here
        self.assertTrue(Palindrome("abcdeffedcba").isPalindrome)  # add assertion here

    def test_longest_palindrome(self):
        self.assertTrue(Palindrome("tattarrattat").isPalindrome)

    def test_not_palindromes(self):
        self.assertFalse(Palindrome("abc").isPalindrome)
        self.assertFalse(Palindrome("Happy").isPalindrome)

    def test_small_pallindrome(self):
        self.assertTrue(Palindrome("aa").isPalindrome)

    def test_onesyllable_palindrome(self):
        pal = Palindrome("a").isPalindrome
        self.assertTrue(pal)
