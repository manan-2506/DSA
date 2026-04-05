class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for i in operations:
            if i == "+":
                res.append(res[-1] + res[-2])
            elif i == "C":
                res.pop()
            elif i == "D":
                i = res[-1]*2
                res.append(i)
            else:
                res.append(int(i))

        return sum(res)