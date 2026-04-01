class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res,curSum = 0,0
        pfs = {0:1}

        for n in nums:
            curSum += n
            diff = curSum-k

            res += pfs.get(diff , 0)
            pfs[curSum] = 1 + pfs.get(curSum ,0)

        return res