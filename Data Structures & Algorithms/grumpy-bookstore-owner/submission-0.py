class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        curr = 0
        i = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                curr += customers[i]
        #print(curr, i)
        left = 0

        res = curr
        while i+1 < len(customers):
            if grumpy[left] == 1:
                curr -= customers[left]
            left += 1
            i += 1
            if grumpy[i] == 1:
                curr += customers[i]
            res = max(res, curr)
        #print(res)

        total = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                total += customers[i]
        return total+res
