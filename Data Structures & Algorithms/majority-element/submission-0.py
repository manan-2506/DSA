class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                    if count > len(nums)/2:
                        return nums[i]
        return nums[0]