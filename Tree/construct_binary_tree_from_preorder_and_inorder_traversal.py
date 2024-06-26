# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ## preorder: root->left->right
        ## inorder: left->root->right
        if preorder == [] or inorder == []:
            return None
        root = TreeNode(val = preorder[0])
        mid = inorder.index(preorder[0])
        ## why preoder not become empty if list is mutable -> mutable is like pass by reference.
        ## However, for the variable in the function passed having same name, which means it creates a new preorder variable and points to the preorder list (just from the start index and end index) and we don't modify the value
        root.left = self.buildTree(preorder[1:1+mid], inorder[:mid])
        root.right = self.buildTree(preorder[1+mid:], inorder[mid+1:])

        return root