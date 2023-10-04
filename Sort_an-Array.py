class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        for i  in nums:
            res.append(i)
        return sorted(res)
