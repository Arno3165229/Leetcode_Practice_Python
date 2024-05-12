class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_interval_list = []
        cur = 0

        for interval in intervals:
            if newInterval[1] < interval[0]:
                new_interval_list.append(interval)
            elif newInterval[0] > interval[1]:
                new_interval_list.append(interval)
                cur += 1
            elif newInterval[0] <= interval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        new_interval_list.insert(cur, newInterval)
        return new_interval_list