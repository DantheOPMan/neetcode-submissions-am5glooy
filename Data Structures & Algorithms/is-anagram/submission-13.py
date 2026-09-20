class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dataS = {}
        dataT = {}


        for i in range(len(s)):
            dataS[s[i]] = dataS.get(s[i],0) + 1
            dataT[t[i]] = dataT.get(t[i],0) + 1

        return dataS == dataT