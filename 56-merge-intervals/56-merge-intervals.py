# Approach: Sorting; Time: O(nlogn+n) ~ O(nlogn); Space: O(1)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step-1: Sort the intervals based on the `start` time
        intervals.sort(key=lambda i:i[0])

        # Take care of the base case
        mergedIntervals = [intervals[0]]

        # Iterate through all the intervals, leaving the first one
        for start, end in intervals[1:]:
            # Get the `end` of the most recently added interval
            lastEnd = mergedIntervals[-1][1]
            # Check if we can merge
            if lastEnd >= start:
                mergedIntervals[-1][1] = max(lastEnd, end) # Update `end`
            else:
                mergedIntervals.append([start, end]) # no overlap, add the interval

        return mergedIntervals