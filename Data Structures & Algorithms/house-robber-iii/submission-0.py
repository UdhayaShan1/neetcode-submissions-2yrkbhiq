# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def dfs(node, skip):
            if node is None:
                return 0
            key = (node, skip)
            if key in dp:
                return dp[key]
            if skip:
                dp[key] = dfs(node.left, False) + dfs(node.right, False)
            else:
                y1 = -float('inf')
                y1 = max(y1, dfs(node.left, False) + dfs(node.right, False))
                y1 = max(y1, dfs(node.left, True) + dfs(node.right, True)+node.val)
                dp[key] = y1

            return dp[key]
        return dfs(root, False)