class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rep = 0

        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[rep]
                nums[rep] = nums[i]
                nums[i] = temp
                rep += 1

        return rep 
