class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dif = {}

        for i, n in enumerate(nums):
            if n in dif:
                return [dif[n], i]
            dif[target - n] = i
        
