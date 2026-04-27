class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i = 0
        j = len(people)-1
        people.sort()
        res = 0
        while i <= j:
            if i == j:
                res += 1
                break
            if people[i] + people[j] > limit:
                res += 1
                j -= 1
            else:
                i += 1
                j -= 1
                res += 1
        return res
