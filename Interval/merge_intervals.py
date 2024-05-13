class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort()
        merged_interval = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] > merged_interval[-1][1]:
                merged_interval.append(intervals[i])
            else:
                if intervals[i][1] > merged_interval[-1][1]:
                    merged_interval[-1][1] = intervals[i][1]

        return merged_interval
                    