class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        arr: the string after appending the char from text 
        returns true if palindrome 
        """
        arr = "".join([ch for ch in s if ch.isalnum()]).lower()
        return arr[::-1] == arr
