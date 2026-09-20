class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsData = set(nums)
        res = 0
        for n in nums:
            if (n-1) in numsData:
                continue
            cur = 0
            while n + cur in numsData:
                cur += 1
            res = max(res, cur)
        return res