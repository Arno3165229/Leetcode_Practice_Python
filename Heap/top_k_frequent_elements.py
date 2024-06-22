class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for number in nums:
            countMap[number] = countMap.get(number, 0) + 1

        ## list index means the frequent values
        frequentList = [[] for i in range(len(nums)+1)]

        for key, value in countMap.items():
            frequentList[value].append(key)

        topK = []
        for i in range(len(frequentList)-1, -1, -1):
            for num in frequentList[i]:
                    topK.append(num)
                    if len(topK) == k:
                         return topK
        