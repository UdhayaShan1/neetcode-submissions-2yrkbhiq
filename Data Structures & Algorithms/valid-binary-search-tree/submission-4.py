# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, big):
            if not node:
                return True
            if not (small < node.val < big):
                return False

            return dfs(node.left, small, min(big, node.val)) and dfs(node.right, max(small, node.val), big)
        return dfs(root, -float('inf'), float('inf'))
