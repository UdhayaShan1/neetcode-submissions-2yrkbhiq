# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        dp = {}
        def lol(find):
            dp = {}
            #print(find.val)
            def contains(node, find):
                if not node:
                    return False
                #print(node.val, find.val, node==find)
                if node.val == find.val:
                    dp[node.val] = True
                    return True
                
                
                dp[node.val] = contains(node.left, find) or contains(node.right, find)
                return dp[node.val]
            contains(root, find)
            return dp

        
        d1 = lol(p)
        d2 = lol(q)
        #print(d1, d2)
        res = [None]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            if res[0] is None and d1.get(node.val, False) and d2.get(node.val, False):
                res[0] = node
        dfs(root)
        return res[0]

        