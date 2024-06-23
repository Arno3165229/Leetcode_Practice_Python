# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0
        
        def dfsHelper(node, curdDepth):
            if node == None:
                return
            curdDepth += 1
            self.maxDepth = max(self.maxDepth, curdDepth)
            dfsHelper(node.left, curdDepth)
            dfsHelper(node.right, curdDepth)

        dfsHelper(root, 0)
        return self.maxDepth