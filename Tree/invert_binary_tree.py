# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfsHelper(node):
            if node == None:
                return
            tmpleft = dfsHelper(node.left)
            tmpright = dfsHelper(node.right)
            node.right = tmpleft
            node.left = tmpright
            return node
    
        return dfsHelper(root)