class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}

        for i, n in enumerate(nums):
            if n in data:
                return [data[n], i]
            data[target - n] = i
        

            