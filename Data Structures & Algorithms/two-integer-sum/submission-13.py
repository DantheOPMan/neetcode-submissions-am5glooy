class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in maps:
                return [maps[dif], i]
            maps[nums[i]] = i

        return []