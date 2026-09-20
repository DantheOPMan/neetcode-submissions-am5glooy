class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        data = {}
        res = 0
        left = 0
        maxCount = 0
        for i in range(len(s)):
            data[s[i]] = data.get(s[i],0) + 1
            maxCount = max(data[s[i]], maxCount)
            while (i - left + 1) - maxCount > k:
                data[s[left]] -=1
                left +=1
            res = max(i-left+1, res)
        
        return res