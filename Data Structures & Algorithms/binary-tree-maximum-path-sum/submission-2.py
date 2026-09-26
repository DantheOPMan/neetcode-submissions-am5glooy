# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            leftMax = max(0, dfs(root.left))
            rightMax = max(0, dfs(root.right))

            res = max(res, leftMax + rightMax + root.val)

            return max(leftMax, rightMax) + root.val

        dfs(root)
        return res