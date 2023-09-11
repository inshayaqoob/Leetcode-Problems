class Solution:
    def splitArray(self, nums, k):
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            splits, subarray_sum = 1, 0
            
            for num in nums:
                subarray_sum += num
                if subarray_sum > mid:
                    subarray_sum = num
                    splits += 1
            
            if splits <= k:
                right = mid
            else:
                left = mid + 1
        
        return left
