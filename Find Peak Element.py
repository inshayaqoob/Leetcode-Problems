class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak_index = 0  # Initialize the peak index to the first element
        for i in range(len(nums)):
            if (i == 0 or nums[i] > nums[i-1]) and (i == len(nums)-1 or nums[i] > nums[i+1]):
                peak_index = i  # Update the peak index when a peak is found
        return peak_index  # Return the index of the last peak encountered
