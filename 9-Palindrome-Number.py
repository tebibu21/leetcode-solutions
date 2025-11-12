class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
    # Numbers ending with 0 but not 0 itself are not palindrome
        if x % 10 == 0 and x != 0:
            return False

        reversed_half = 0
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # For even-length and odd-length numbers
        return x == reversed_half or x == reversed_half // 10