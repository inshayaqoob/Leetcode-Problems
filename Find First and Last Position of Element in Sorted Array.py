class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]  # Initialize result with -1 for both indices

        # Find the starting index
        for i in range(len(nums)):
            if nums[i] == target:
                result[0] = i
                break  # Stop when the first occurrence is found

        # Find the ending index
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                result[1] = i
                break  # Stop when the last occurrence is found

        return result
