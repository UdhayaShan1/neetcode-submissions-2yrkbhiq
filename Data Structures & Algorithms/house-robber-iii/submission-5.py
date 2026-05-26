# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        from functools import cache
        @cache
        def dfs(node, taken):
            if not node:
                return 0
            if taken:
                return dfs(node.left, not taken)+dfs(node.right, not taken)
            take = node.val+dfs(node.left, not taken)+dfs(node.right, not taken)
            not_take = dfs(node.left, taken)+dfs(node.right, taken)
            return max(take, not_take)
        return dfs(root, False)