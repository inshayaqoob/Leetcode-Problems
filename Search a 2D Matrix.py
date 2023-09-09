class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_found = any(target in subarray for subarray in matrix)
        if target_found:
            return True
        else:
            return False
        