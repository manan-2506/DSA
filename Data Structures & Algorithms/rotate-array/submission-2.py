class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(a,b):
            while a<b:
                temp = nums[a]
                nums[a] = nums[b]
                nums[b] = temp
                a += 1
                b -= 1
        
        n = len(nums)-1
        k = k % (n+1)
        rev(0,n-k)
        rev(n-k+1,n)
        rev(0,n)