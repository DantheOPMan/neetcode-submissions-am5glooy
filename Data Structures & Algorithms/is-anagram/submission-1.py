class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}
        for n in range(len(s)):
            if s[n] not in countS:
                countS[s[n]] = 1
            else:
                countS[s[n]] += 1
        
            if t[n] not in countT:
                countT[t[n]] = 1
            else:
                countT[t[n]] += 1

        return countT == countS
