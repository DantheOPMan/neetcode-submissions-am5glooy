class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i, c in enumerate(nums):
            if c in data:
                return [data[c], i]
            dif = target - c
            data[dif] = i
        return []