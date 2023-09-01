class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        checker = ''.join(sorted(s1))
        
        for i in range(len(s2) - len(s1)+1):
            temp = ''.join(sorted(s2[i:i+len(s1)]))
            if temp == checker:
                return True
        return False