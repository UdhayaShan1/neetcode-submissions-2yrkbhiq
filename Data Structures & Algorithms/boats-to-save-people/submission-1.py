class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people)-1
        res = 0
        while i <= j:
            if i == j:
                res += 1
                break
            s = people[i]+people[j]
            if s <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            res += 1
        return res

