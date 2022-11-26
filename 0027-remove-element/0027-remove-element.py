# One-pass, 2-Pointer approach ; Space: O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numOfDuplicates = 0
        start, end = 0, len(nums)-1
        while start <= end:
            # Look for `val` on the left
            while start < len(nums) and nums[start] != val:
                start += 1
            # Look for non-`val` on the right
            while end >=0 and nums[end] == val:
                numOfDuplicates += 1
                end -= 1
            # Swap if both `start` and `end` are in range
            if start < len(nums) and end >=0 and start < end:
                numOfDuplicates += 1
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                # Update `start` and `end`
                start += 1
                end -= 1
            else:
                break

        return len(nums) - numOfDuplicates