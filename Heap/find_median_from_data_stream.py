class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1*num)
        if self.small and self.large and -1*self.small[0] > self.large[0]:
            tmp = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*tmp)
        
        if len(self.large) > len(self.small)+1:
            tmp = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*tmp)
        
        if len(self.small) > len(self.large)+1:
            tmp = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*tmp)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-1*self.small[0] + self.large[0])/2
        else:
            return -1*self.small[0] if len(self.small) > len(self.large) else self.large[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()