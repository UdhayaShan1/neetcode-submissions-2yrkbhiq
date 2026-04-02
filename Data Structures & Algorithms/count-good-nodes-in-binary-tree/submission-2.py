# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, m):
            if not node:
                return 0
            r = 1
            if node.val < m:
                r = 0
            return r+dfs(node.left, max(node.val, m))+dfs(node.right, max(node.val, m)) 
        return dfs(root, -float('inf'))
        