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
                return -1

            dp[node] = max(dfs(node.left)+1, dfs(node.right)+1)
            return dp[node]
        dfs(root)
        print(dp)
        def dfs(node):
            if not node:
                return True
            
            left_height = -1
            right_height = -1
            if node.left:
                left_height = dp[node.left]
            if node.right:
                right_height = dp[node.right]
            #print(node.val, left_height, right_height)
            if left_height == -1 and right_height > 0:
                return False
            if right_height == -1 and left_height > 0:
                return False
            if left_height == -1 and right_height == -1:
                return True
            if abs(left_height - right_height) > 1:
                return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)
