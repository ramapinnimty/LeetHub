# Time: O(m + n); Space: O(1)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []

        ptr1, ptr2 = 0, 0
        while ptr1 < len(firstList) and ptr2 < len(secondList):
            s1, e1 = firstList[ptr1][0], firstList[ptr1][1]
            s2, e2 = secondList[ptr2][0], secondList[ptr2][1]
            # Check if there's any intersection (applies to all the 6 cases)
            lo, hi = max(s1, s2), min(e1, e2)
            if lo <= hi:
                intersections.append([lo, hi])
            # Adjust (increment) the pointers based on the higher e1 or e2
            if e1 > e2:
                ptr2 += 1
            else:
                ptr1 += 1

        return intersections