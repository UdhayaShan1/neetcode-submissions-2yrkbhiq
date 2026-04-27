# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr):
            if node is None:
                return 0
            
            y1 = 0
            if node.val >= curr:
                y1 = 1
            y1 += dfs(node.left, max(curr, node.val))+dfs(node.right, max(curr, node.val))
            return y1
        return dfs(root, -float('inf'))
