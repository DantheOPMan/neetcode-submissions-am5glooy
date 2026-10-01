class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs(cur, left):
            if not len(left) and len(cur) == len(nums):
                res.append(cur)
                return
            
            for i in range(len(left)):
                nextSet = cur.copy() + [left[i]]

                dfs(nextSet, left[:i] + left[i+1:])

        dfs([], nums)
        return res