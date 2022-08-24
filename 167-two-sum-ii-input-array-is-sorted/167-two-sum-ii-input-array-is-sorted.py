# Approach: Two Pointers; Time: O(n); Space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start < end:
            # Calculate the sum of numbers at `start` & `end`
            curr_sum = numbers[start] + numbers[end]
            # Update `end` if we have a greater sum
            if curr_sum > target:
                end -= 1
            # Update `start` if we have a lesser sum
            elif curr_sum < target:
                start += 1
            else:
                return [start+1, end+1] # we found the result pair!