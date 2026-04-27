# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummy = TreeNode()
        dummy.left = root

        def getRightMost(node):
            if node.right == None:
                return node
            
            return getRightMost(node.right)

        def getLeftMost(node):
            if node.left == None:
                return node
            
            return getLeftMost(node.left)
        #print(getRightMost(root).val)

        def dfs(node):
            if not node:
                return
            if node.left and node.left.val == key:
                ref = node.left
                if not ref.left and not ref.right:
                    node.left = None
                elif not ref.left:
                    node.left = ref.right
                elif not ref.right:
                    node.left = ref.left
                else:
                    tmp = getRightMost(ref.left)
                    node.left = ref.left
                    tmp.right = ref.right
            elif node.right and node.right.val == key:
                ref = node.right
                if not ref.left and not ref.right:
                    node.right = None
                elif not ref.left:
                    node.right = ref.right
                elif not ref.right:
                    node.right = ref.left
                else:
                    tmp = getLeftMost(ref.right)
                    node.right = ref.right
                    tmp.left = ref.left
                
            
            dfs(node.left)
            dfs(node.right)
        dfs(dummy)
        return dummy.left

                