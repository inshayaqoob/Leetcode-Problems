class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda num: abs(num - x))  # Sort by absolute difference from x
        return sorted(arr[:k])