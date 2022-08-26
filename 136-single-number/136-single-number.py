# Approach: Bit manipulation; Time: O(n); Space: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Iterate the complete list while xor-ing
        unique_num = 0 # since `num` XOR `0` = `num`
        for num in nums:
            unique_num ^= num

        return unique_num # we'll end up with the unique number