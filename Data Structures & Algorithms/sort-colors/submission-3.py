class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(n ,m):
            temp = nums[n]
            nums[n] = nums[m]
            nums[m] = temp

        low , i , high = 0 , 0 , len(nums)-1 

        while i <= high:
            if nums[i] == 0:
                swap(low,i)
                low += 1
            elif nums[i] == 2:
                swap(high , i)
                high -= 1
                i -= 1
            i += 1

        return nums
                