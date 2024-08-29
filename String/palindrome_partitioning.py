class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPali(s, i, j):
            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True


        def dfsBacktracking(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfsBacktracking(j+1)
                    part.pop()
        
        dfsBacktracking(0)

        return res
                