class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs(cur, left):
            if not left:
                res.append(cur)
                return
            
            for i in range(len(left)):
                dfs(cur + [left[i]], left[:i] + left[i+1:])

        dfs([], nums)
        return res