class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        k = 1
        i = 1

        while i < len(nums):
            if nums[i] != nums[l]:
                l += 1
                tmp = nums[i]
                nums[i] = nums[l]
                nums[l] = tmp
                k += 1
            i += 1
        return k