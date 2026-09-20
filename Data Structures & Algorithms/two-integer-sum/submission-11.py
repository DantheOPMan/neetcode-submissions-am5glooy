class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}

        for i, n in enumerate(nums):
            dif = target - n
            if n in data:
                return [data[n], i]
            data[dif] = i
