class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = [0]*1000000

        for i in nums:
            if i<len(ans):
                ans[i] += 1
        
        for i in range(1,len(ans)):
            if ans[i] == 0:
                return i