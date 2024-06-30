# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        ## inorder: left->root->right
        encode = []

        def dfsHelper(node):
            if node == None:
                encode.append("null")
                return
            encode.append(str(node.val)) 
            dfsHelper(node.left)           
            dfsHelper(node.right)

        dfsHelper(root)
        return ",".join(encode)
    
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ##[1, 2, null, null, 3, 4, null, null, 5, null, null]
        

    def deserialize(self, data):
        encodeList = list(data.split(","))
        self.c = 0
        def dfsHelper(value):
            if value == "null":
                self.c += 1
                return None
            root = TreeNode(int(value))
            self.c += 1
            root.left = dfsHelper(encodeList[self.c])
            root.right = dfsHelper(encodeList[self.c])
            return root
        
        return dfsHelper(encodeList[self.c])

        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))