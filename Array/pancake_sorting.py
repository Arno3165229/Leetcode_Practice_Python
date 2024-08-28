class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        lenArr = len(arr)

        for i in range(lenArr):
            tmpMax = max(arr[:lenArr-i])
            tmpMaxIndex = arr.index(tmpMax)
            arr = self.reverseUptoK(arr, tmpMaxIndex)
            res.append(tmpMaxIndex+1)

            arr = self.reverseUptoK(arr, lenArr-i-1)
            res.append(lenArr-i)
        
        return res

    def reverseUptoK(self, arr, k):
        arr = arr[:k+1][::-1] + arr[k+1:]
        return arr