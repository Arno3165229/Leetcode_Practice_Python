# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.splitMax = float("-inf")

        def dfsHelper(node):
            if node == None:
                return 0
            leftmax = dfsHelper(node.left)
            rightmax = dfsHelper(node.right)
            leftmax = max(0, leftmax)
            rightmax = max(0, rightmax)
            ## split
            self.splitMax = max(node.val+leftmax+rightmax, self.splitMax)
            ## not split
            return node.val + max(leftmax, rightmax)
        
        return max(dfsHelper(root), self.splitMax)