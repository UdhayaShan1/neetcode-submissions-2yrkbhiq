class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        curr = 0
        most = -float('inf')
        for i in range(minutes):
            if grumpy[i] == 1:
                curr += customers[i]
        
        left = 0
        right = minutes-1
        while True:
            most = max(most, curr)
            if right+1 >= len(customers):
                break
            if grumpy[left] == 1:
                curr -= customers[left]
            if grumpy[right+1] == 1:
                curr += customers[right+1]
            left += 1
            right += 1
        #print(most)
        
        total = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total += customers[i]
        #print(total)
        return total+most

