class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.get_alphanum_only(s)
        print(s)
        if s != ''.join(s[::-1]):
            return False
        return True

    def get_alphanum_only(self, s):
        return ''.join([char for char in s if char.isalnum()]).lower()