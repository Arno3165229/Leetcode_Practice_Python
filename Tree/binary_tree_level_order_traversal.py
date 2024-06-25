# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: ## Time complexity O(N), Memory complexity O(N)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        levelOrder = [[]] ## remember here is 2d list

        def dfsHelper(node, level):
            if not node:
                return
            if len(levelOrder) < level+1:
                levelOrder.append([])
            levelOrder[level].append(node.val)
            dfsHelper(node.left, level+1)
            dfsHelper(node.right, level+1)
        
        dfsHelper(root, 0)

        return levelOrder
            
