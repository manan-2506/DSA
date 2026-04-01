class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxC = 0
        nu = set(nums)
        for n in nu:
            count = 0
            if n-1 not in nu:
                count = 0
                while n+count in nu:
                    count += 1
                maxC = max(maxC,count)

        return maxC