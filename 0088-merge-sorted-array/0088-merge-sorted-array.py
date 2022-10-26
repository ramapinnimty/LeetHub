class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def rshift(idx, end):
            ptr = end
            while ptr > idx:
                nums1[ptr] = nums1[ptr-1]
                ptr -= 1

        ptr1, ptr2 = 0, 0
        end_ptr = m
        while ptr1 < end_ptr and ptr2 < n:
            if nums2[ptr2] <= nums1[ptr1]:
                rshift(ptr1, end_ptr)
                end_ptr += 1
                nums1[ptr1] = nums2[ptr2]
                ptr1, ptr2 = ptr1+1, ptr2+1
            else:
                ptr1 += 1
        if ptr2 < n:
            while ptr2 < n:
                nums1[end_ptr] = nums2[ptr2]
                end_ptr, ptr2 = end_ptr+1, ptr2+1