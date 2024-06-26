# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## time complexity O(M*N), memory complexity O(N)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSametree(root, subRoot):
            return True
        if not root:
            return False
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    def isSametree(self, nodeP, nodeQ):
        if not nodeP and not nodeQ:
            return True
        if not nodeP or not nodeQ:
            return False
        if nodeP.val != nodeQ.val:
            return False
        return (self.isSametree(nodeP.left, nodeQ.left)) and (self.isSametree(nodeP.right, nodeQ.right))