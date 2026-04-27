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
                return 0
            
            dp[node] = max(dfs(node.left)+1, dfs(node.right)+1)
            return dp[node]
        dfs(root)
        #print(dp)

        def dfs(node):
            if node is None:
                return 0
            l = 0 if node.left is None else dp[node.left]
            r = 0 if node.right is None else dp[node.right]

            #return max()
            return max(l+r, dfs(node.left), dfs(node.right))
        return dfs(root)

            