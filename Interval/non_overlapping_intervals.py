class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        
        intervals.sort()
        prev = 0
        result = 0

        for interval in intervals[1:]:
            if interval[0] < intervals[prev][1]:
                result += 1
                if interval[1] <= intervals[prev][1]:
                    prev += 1 ## DON'T use this method since sometime it will jump over 1 and directly to the previous compared index
            else:
                prev += 1 ## DON'T use this method since sometime it will jump over 1 and directly to the previous compared index
        
        return result
    

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        
        intervals.sort()
        prev = 0
        result = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[prev][1]:
                result += 1
                if intervals[i][1] <= intervals[prev][1]:
                    prev = i
            else:
                prev = i
        
        return result