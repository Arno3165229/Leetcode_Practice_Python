class TreeNode:
    def __init__(self):
        self.childlist = {}
        self.endofword = False

class WordDictionary:
    def __init__(self):
        self.root = TreeNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.childlist:
                cur.childlist[c] = TreeNode()
            cur = cur.childlist[c]
        cur.endofword = True
        
    def search(self, word: str) -> bool:
        cur = self.root

        def dfsHelper(cur, start):
            for index in range(start, len(word)):
                if word[index] == '.':
                    for node in cur.childlist.values():
                        if dfsHelper(node, index+1):
                            return True
                if word[index] not in cur.childlist:
                    return False
                cur = cur.childlist[word[index]]
            return cur.endofword

        return dfsHelper(cur, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)