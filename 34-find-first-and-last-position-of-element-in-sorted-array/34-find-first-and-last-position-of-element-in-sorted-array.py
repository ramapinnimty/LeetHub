# Approach: 2-pass Binary search; Time: O(logn); Space: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find the left-most occurrence
        leftmost_idx  = self.BSUtil(nums, target, 'left')
        # Find the right-most occurrence
        rightmost_idx = self.BSUtil(nums, target, 'right')

        ###   NOT REQUIRED   ###
#         if leftmost_idx  == rightmost_idx:
#             return [-1, -1]

#         if leftmost_idx == -1 or rightmost_idx == -1:
#             return [-1, -1]
        ###   NOT REQUIRED   ###

        return [leftmost_idx, rightmost_idx]

    def BSUtil(self, nums, target, dir='left'):
        start, end = 0, len(nums)-1
        found_idx  = -1
        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                # Modification from traditional BS is here
                found_idx = mid # keep updating the found index
                if dir == 'left':
                    end = mid - 1 # look only left
                elif dir == 'right':
                    start = mid + 1 # look only right

        return found_idx