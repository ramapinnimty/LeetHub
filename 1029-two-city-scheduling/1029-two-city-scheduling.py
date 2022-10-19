# Approach: Greedy ; Time: O(nlogn); Space: O(n) for sorting in Python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # STEP-1: Sort the costs in ASC order based on Cost_A - Cost_B
        costs.sort(key=lambda cost : cost[0]-cost[1])

        # STEP-2(a): Sum up the costs for City_A
        minCost = 0
        for idx in range(0, len(costs)//2):
            minCost += costs[idx][0]

        # STEP-2(b): Sum up the costs for City_B
        for idx in range(len(costs)//2, len(costs)):
            minCost += costs[idx][1]

        return minCost