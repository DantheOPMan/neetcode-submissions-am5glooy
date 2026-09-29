class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            current = res[:]
            for subset in current:
                res.append(subset + [num])

        return res