class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}

        res = []
        def dfsBacktracking(i, curString):
            if len(curString) == len(digits):
                res.append(curString)
                return
            
            for c in map[digits[i]]:
                dfsBacktracking(i+1, curString+c)
        
        if digits:
            dfsBacktracking(0, "")
        
        return res