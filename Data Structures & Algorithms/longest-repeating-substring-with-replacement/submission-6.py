class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        data = {}
        maxCount = 0
        left = 0
        res = 0
        for i, n in enumerate(list(s)):
            data[n] = data.get(n,0) + 1
            maxCount = max(maxCount, data[n])
            while (i - left + 1) - maxCount > k:
                data[s[left]] -= 1
                left += 1
            res = max(res, i - left + 1 )
        
        return res