class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)
        res = 0

        for i in data:
            if i-1 not in data:
                length = 1
                while (i + length) in data:
                    length +=1
                res = max(length, res)
        
        return res