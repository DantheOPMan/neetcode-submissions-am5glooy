class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        cur = []
        def dfs(left):
            if not left:
                res.append(cur.copy())
                return
            
            for i in range(len(left)):
                chosen = left.pop(i)
                cur.append(chosen)
                dfs(left)
                cur.pop()
                left.insert(i, chosen)
        dfs(nums.copy())
        return res