from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        if not intervals:
            return 0
        
        timehash = {}

        for interval in intervals:
            timehash[interval.start] = timehash.get(interval.start, 0) + 1
            timehash[interval.end] = timehash.get(interval.end, 0) - 1

        ## hashmap cannot use .sort()
        listTimehash = list(timehash.items())
        listTimehash.sort(key=lambda tuple : tuple[0])

        curRoom = 0
        maxRoom = 0
        for time in listTimehash:
            curRoom += time[1]
            maxRoom = max(curRoom, maxRoom)

        return maxRoom
