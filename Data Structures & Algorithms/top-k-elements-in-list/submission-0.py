class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [0]*k
        count = [0]*2000

        for num in nums:
            count[num+1000] += 1
                

        for i in range(k):
            maxval = count.index(max(count)) 
            res[i] = (maxval - 1000)
            count[maxval] = 0

        return res