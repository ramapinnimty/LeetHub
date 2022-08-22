# Time: O(n); Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L = len(nums)
        # Check if there's only 1 element
        if L == 1:
            return nums[0]

        # Set the initial maximum subarray sum to the first element
        max_sum  = nums[0]
        # Set the initial current sum to 0
        curr_sum = 0
        # Linearly iterate through contiguous subarrays
        for i in range(0, L):
            curr_sum += nums[i] # add the incoming element
            max_sum = max(max_sum, curr_sum) # update max. if necessary
            # Reset the current sum if it is -ve
            if curr_sum < 0:
                curr_sum = 0

        return max_sum