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
            if not node:
                return -1
            dp[node] = max(dfs(node.left)+1, dfs(node.right)+1)
            return dp[node]
        dfs(root)
        #print(dp)

        def dfs(node, res):
            if not node:
                return res
            left = 0 if node.left == None else 1+dp[node.left]
            right = 0 if node.right == None else 1+dp[node.right]
            return max(dfs(node.left, max(res, left+right)), dfs(node.right, max(res, left+right)))
        return dfs(root, 0)

