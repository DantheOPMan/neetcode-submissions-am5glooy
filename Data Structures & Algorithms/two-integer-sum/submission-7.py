class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in data:
                return [data[dif], i]
            data[nums[i]] = i
        