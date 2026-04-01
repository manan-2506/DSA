class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        if len(count) > 2:
            newCount = defaultdict(int)
            for n,c in count.items():
                if c > 1:
                    c -= 1
                    newCount[n] = c
            count = newCount

        res = []
        for i in count:
            if nums.count(i) > len(nums)//3:
                res.append(i)
        
        return res