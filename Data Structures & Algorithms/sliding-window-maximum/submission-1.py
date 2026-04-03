class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        r = l+k
        
        while r < len(nums)+1:
            maxl = -float("infinity")
            t = l
            while t<r:
                maxl = max(maxl,nums[t])
                t += 1
            res.append(maxl)

            l += 1
            r += 1

        return res