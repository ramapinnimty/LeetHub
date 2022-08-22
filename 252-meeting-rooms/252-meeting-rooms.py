# Time: O(nlogn); Space: O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort the intervals based on the start time
        intervals.sort(key = lambda pair : pair[0])

        # Time: O(n); Compare every adjacent pair
        for idx in range(0, len(intervals)-1):
            # Check if end[i] > start[j] where i<j
            if intervals[idx][1] > intervals[idx+1][0]:
                return False

        return True # could attend all meetings