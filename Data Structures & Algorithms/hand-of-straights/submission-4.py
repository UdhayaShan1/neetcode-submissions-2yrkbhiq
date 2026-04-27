class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = {}
        for i in hand:
            c[i] = c.get(i, 0)+1
        hand.sort()
        for i in hand:
            if c[i] == 0:
                continue
            for j in range(i, i+groupSize):
                if j not in c or c[j] == 0:
                    return False
                c[j] -= 1
        return True
