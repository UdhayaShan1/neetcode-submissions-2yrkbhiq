# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            dfs(node.right)
            l = node.left
            r = node.right
            if l and not l.left and not l.right and l.val == target:
                node.left = None
            if r and not r.left and not r.right and r.val == target:
                node.right = None
            #print(node.val)
            # if node.val == target:
            #     print(node.val, '@')
        dfs(root)
        if root and root.val == target and not root.left and not root.right:
            return None

        return root