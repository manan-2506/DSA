class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res , ans = [] , 0

        for i in operations:
            if i == "+":
                ans += res[-1] + res[-2]
                res.append(res[-1] + res[-2])
            elif i == "C":
                ans -= res.pop()
            elif i == "D":
                ans += (2*res[-1]) 
                res.append(res[-1]*2)
            else:
                ans += int(i)
                res.append(int(i))

        return ans