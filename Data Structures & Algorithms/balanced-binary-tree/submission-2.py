# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        dp = {}
        def dfs(node):
            if not node:
                return 0
            dp[node] = max(dfs(node.left)+1, dfs(node.right)+1)
            return dp[node]
        dfs(root)
        print(dp)

        def dfs(node):
            if not node:
                return True
            
            l = 0
            if node.left:
                l = dp[node.left]
            r = 0
            if node.right:
                r = dp[node.right]
            if abs(l-r) > 1:
                return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)


        