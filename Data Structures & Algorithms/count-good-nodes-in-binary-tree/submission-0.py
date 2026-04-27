# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        chk = {}
        def dfs(node, curr):
            if not node:
                return
            chk[node] = max(node.val, curr)
            dfs(node.left, max(curr, node.val))
            dfs(node.right, max(curr, node.val))
        dfs(root, -float('inf'))
        #print(chk)
        count = 0
        for i in chk:
            if chk[i] <= i.val:
                count += 1
        return count
            
