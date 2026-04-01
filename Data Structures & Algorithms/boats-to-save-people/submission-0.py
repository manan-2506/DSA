class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = 0
        l = 0
        r = len(people)-1
        people.sort()

        while l<=r:
            if l == r:
                n += 1
                break
            if people[l]+people[r] > limit:
                    n += 1
                    r -= 1
            else:
                n += 1
                l += 1
                r -= 1
        return n