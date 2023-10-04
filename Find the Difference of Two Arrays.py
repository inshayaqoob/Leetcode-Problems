class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer1_set = set()
        answer2_set = set()
        
        for i in nums1:
            if i not in nums2:
                answer1_set.add(i)
        
        for i in nums2:
            if i not in nums1:
                answer2_set.add(i)
        
        return [list(answer1_set), list(answer2_set)]
