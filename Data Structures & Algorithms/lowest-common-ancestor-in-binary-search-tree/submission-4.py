# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find(n):
            dp = {}
            def dfs(node):
                if not node:
                    return False
                if node.val == n.val:
                    dp[node.val] = True
                    return True

                dp[node.val] = dfs(node.left) or dfs(node.right)
                return dp[node.val]
            dfs(root)
            return dp
        d1 = find(p)
        d2 = find(q)

        res = [None]
        def dfs(node):
            if not node:
                return
            if d1.get(node.val, False) and d2.get(node.val, False):
                res[0] = node
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res[0]