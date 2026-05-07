class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left = 0
        print(sum([1,0,1,2,1,1,7,5]))
        actual = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                actual += customers[i]
        print(actual)

        most = 0
        left = 0
        g = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 1:
                g += customers[i]
            while i-left+1 > minutes:
                if grumpy[left] == 1:
                    g -= customers[left]
                left += 1
            if i-left+1 == minutes:
                most = max(most, g)
        return actual+most
