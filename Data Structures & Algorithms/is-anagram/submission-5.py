class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        frq = {}

        for c in s:
            frq[c] = frq.get(c, 0) + 1
        for c in t:
            if c not in frq:
                return False
            if frq[c] <= 0:
                return False
            frq[c] -= 1
        
        return True