# Time: O(n) + O(nlogn); Space: O(1) in Python as heapify() happens in-place
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Simulate a Max-Heap
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)

        # Smash stones till we end up with either 0 or 1 stones
        while len(stones) > 1:
            # Get the 1st max. element [TC: O(logn)]
            y = abs(heapq.heappop(stones))
            # Get the 2nd max. element [TC: O(logn)]
            x = abs(heapq.heappop(stones))
            # Push the difference of unequal weights into the heap
            if y != x:
                # [TC: O(logn)]
                heapq.heappush(stones, -1 * (y-x))

        # Return the only stone left or no stones otherwise
        return -1 * stones[0] if len(stones) == 1 else 0