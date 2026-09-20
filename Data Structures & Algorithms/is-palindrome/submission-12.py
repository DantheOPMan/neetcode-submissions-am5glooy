class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlpha(s):
            return ord('a') <= ord(s) <= ord('z') or ord('A') <= ord(s) <= ord('Z') or ord('0') <= ord(s) <= ord('9')

        l = 0
        r = len(s) -1

        while l < r:
            while not isAlpha(s[l]) and l < r:
                l+=1
            while not isAlpha(s[r]) and l < r:
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -=1
        return True