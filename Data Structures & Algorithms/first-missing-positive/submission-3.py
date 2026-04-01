class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = 1

        for i in range(len(nums)+1):
            if n not in nums and n > 0 and n <= len(nums):
                return n
            else:
                n += 1
        return len(nums)+1 