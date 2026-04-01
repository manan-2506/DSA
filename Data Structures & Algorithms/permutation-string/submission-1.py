class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        c1 , c2 = [0]*26 , [0]*26
        matches = 0
        l = 0

        for i in range(len(s1)):
            c1[ord(s1[i])-ord('a')] += 1
            c2[ord(s2[i])-ord('a')] += 1

        for i in range(26):
            if c1[i] == c2[i]:
                matches += 1

        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            
            ind = ord(s2[r]) - ord('a')

            c2[ind] += 1
            if c1[ind] == c2[ind]:
                matches += 1
            elif c1[ind]+1 == c2[ind]:
                matches -= 1
            
            
            ind = ord(s2[l]) - ord('a')

            c2[ind] -= 1
            if c1[ind] == c2[ind]:
                matches += 1
            elif c1[ind]-1 == c2[ind]:
                matches -= 1
            
            l += 1

        return matches == 26