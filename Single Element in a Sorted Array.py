class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        result = set()
        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.add(num)
        return result.pop()



        