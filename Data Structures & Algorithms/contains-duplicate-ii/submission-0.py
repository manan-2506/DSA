class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        frq = {}

        for i in range(len(nums)):
            if nums[i] in frq and i - frq[nums[i]] <= k:
                return True
            frq[nums[i]] = i

        return False  