# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(node1, node2):
            if (node1 and not node2) or (not node1 and node2):
                return False
            if node1 and node2 and node1.val != node2.val:
                return False
            if not node1 and not node2:
                return True
            return equal(node1.left, node2.left) and equal(node1.right, node2.right)
        
        def dfs(node):
            if not node:
                return False
            if node.val == subRoot.val:
                if equal(node, subRoot):
                    return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
                