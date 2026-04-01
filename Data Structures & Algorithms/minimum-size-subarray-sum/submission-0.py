class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total=0,0
        size = float("infinity")

        for i in range(len(nums)):
            total += nums[i]

            while total >= target:
                size = min(size,i-l+1)
                total -= nums[l]
                l += 1

        if size == float("infinity"):
            return 0
        else:
            return size