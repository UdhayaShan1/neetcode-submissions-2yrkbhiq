# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parent = {}
        height = {}
        ref = [None, None]
        def dfs(node, prev, length):
            if not node:
                return
            if node.val == p.val:
                ref[0] = node
            if node.val == q.val:
                ref[1] = node
            parent[node] = prev
            height[node] = length
            dfs(node.left, node, length+1)
            dfs(node.right, node, length+1)
        dfs(root, None, 0)

        #print(parent)
        p = ref[0]
        q = ref[1]
        while p != q:
            print(p.val, q.val)
            if height[p] > height[q]:
                p = parent[p]
            elif height[q] > height[p]:
                q = parent[q]
            else:
                p = parent[p]
                q = parent[q]
            

        return p