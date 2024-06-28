# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k

        def dfsHelper(node):
            if node == None:
                return
            dfsHelper(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            dfsHelper(node.right)

        dfsHelper(root)
        return self.result