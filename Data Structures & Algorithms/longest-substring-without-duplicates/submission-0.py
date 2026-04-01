class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l += 1    
            res.add(s[r])
            result = max(result , r-l+1)

        return result  