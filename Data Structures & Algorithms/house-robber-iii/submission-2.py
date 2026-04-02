# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def dfs(node, taken):
            if not node:
                return 0
            key = (node, taken)
            if key in dp:
                return dp[key]
            res = 0
            if taken:
                res = max(res, dfs(node.left, False)+dfs(node.right, False))
            else:
                res = max(res, node.val + dfs(node.left, True) + dfs(node.right, True))
                res = max(res, dfs(node.left, False)+dfs(node.right, False))
            dp[key] = res
            return res
        return dfs(root, False)


        