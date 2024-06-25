# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min = float("-inf")
        max = float("inf")

        def dfsHelper(node, min, max):
            if not node:
                return True
            if node.val <= min or node.val >= max:
                return False
            if not dfsHelper(node.left, min, node.val) or not dfsHelper(node.right, node.val, max):
                return False
            return True
        
        return dfsHelper(root, min, max)