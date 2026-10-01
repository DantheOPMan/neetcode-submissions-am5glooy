class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs(cur, left):
            if not left:
                res.append(cur)
                return
            
            for i in range(len(left)):
                nxt = left.copy()
                nxt.pop(i)
                dfs(cur + [left[i]], nxt)

        dfs([], nums)
        return res