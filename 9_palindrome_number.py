class Solution:
    def isPalindromeEasy(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x in range(9):
            return True
        else:
            return str(x) == str(x)[::-1]

