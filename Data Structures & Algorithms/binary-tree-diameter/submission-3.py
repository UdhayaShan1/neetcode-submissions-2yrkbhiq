# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def dfs(node):
            if node is None:
                return -1
            dp[node] = max(dfs(node.left)+1, dfs(node.right)+1)
            return dp[node]
        dfs(root)
        #print(dp)

        res = [-float('inf')]
        def dfs(node):
            if node is None:
                return
            l = 0 if node.left is None else 1+dp[node.left]
            r = 0 if node.right is None else 1+dp[node.right]
            res[0] = max(res[0], l+r)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return res[0]
