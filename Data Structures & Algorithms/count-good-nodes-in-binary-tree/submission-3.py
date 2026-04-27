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
            
            res = 1 if node.val >= m else 0
            return res + dfs(node.left, max(m, node.val)) + dfs(node.right, max(m, node.val))
        return dfs(root, -float('inf'))