class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        middleInt = {}
        for i in range(len(nums)):
            if nums[i] in middleInt:
                return [middleInt[nums[i]], i]
            middleInt[(target-nums[i])] = i
