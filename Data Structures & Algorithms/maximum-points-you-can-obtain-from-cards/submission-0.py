class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        smallest = float('inf')
        curr = 0
        for i in range(len(cardPoints)-k):
            curr += cardPoints[i]
        total = sum(cardPoints)
        left = 0
        right = len(cardPoints)-k-1
        while True:
            smallest = min(smallest, curr)
            if right+1 >= len(cardPoints):
                #print(smallest, total)
                return total-smallest
            curr -= cardPoints[left]
            curr += cardPoints[right+1]
            left += 1
            right += 1
