# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfsHelper(p, q):
            if (p and not q) or (not p and q):
                return False
            
            if (p and q) and (p.val != q.val):
                return False
            
            if not p and not q:
                return True
             
            return dfsHelper(p.left, q.left) and dfsHelper(p.right, q.right)
        
        return dfsHelper(p, q)