class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)
        res = 0
        for n in data:
            if n-1 not in data:
                length = 0
                while n + length in data:
                    length +=1
                res = max(res, length)

        return res