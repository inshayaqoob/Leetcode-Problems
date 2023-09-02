class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        ma=0
        for i in range(l,len(s)-l):
            p=s[l:i+1]
            if(len(p)==len(set(p))):
                ma=max(len(p),ma)
            else:
                l+=1
        return ma