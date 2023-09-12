class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        for i in nums1:
            res.append(i)
        for i in nums2:
            res.append(i)
        new = sorted(res)
        l, r = 0, len(new) - 1
        mid = (l + r) / 2

        if len(new) % 2 == 0:
            # If the length is even, return the average of the two middle elements
            mid = (new[l + len(new) // 2] + new[l + len(new) // 2 - 1]) / 2
        else:
            # If the length is odd, return the middle element
            mid = new[l + len(new) // 2]

        return mid
