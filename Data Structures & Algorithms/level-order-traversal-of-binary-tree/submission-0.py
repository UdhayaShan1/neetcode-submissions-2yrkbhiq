# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from queue import Queue
        res = {}
        def bfs():
            q = Queue()
            q.put((root, 0))
            res[0] = [root.val]

            while not q.empty():
                curr = q.get()
                curr_node = curr[0]
                curr_h = curr[1]
                if curr_h+1 not in res:
                    res[curr_h+1] = []
                if curr_node.left:
                    res[curr_h+1].append(curr_node.left.val)
                    q.put((curr_node.left, curr_h+1))
                if curr_node.right:
                    res[curr_h+1].append(curr_node.right.val)
                    q.put((curr_node.right, curr_h+1))
        bfs()
        #print(res)
        final = []
        for i in res:
            if len(res[i]) == 0:
                break
            final.append(res[i])
        return final
                



