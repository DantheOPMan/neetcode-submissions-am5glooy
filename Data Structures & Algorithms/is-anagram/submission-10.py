class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False
        dataS = defaultdict(int)
        dataT = defaultdict(int)
        for c in range(len(s)):
            dataS[s[c]] = dataS.get(s[c],0) +1
            dataT[t[c]] = dataT.get(t[c],0) +1

        return dataS == dataT