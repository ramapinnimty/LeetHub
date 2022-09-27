# Approach: Min Heap; Time: O(n + k logn); Space: O(n)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create [distance_from_origin, point]
        # NOTE: I used (x^2 + y^2) for distance from O to ease computations
        pointDistList = []
        for point in points:
            heapq.heappush(pointDistList, (point[0]**2 + point[1]**2, point))

        # Create the result list with `k` closest points
        kClosestPoints = []
        while k > 0:
            kClosestPoints.append(heapq.heappop(pointDistList)[1])
            k -= 1

        return kClosestPoints