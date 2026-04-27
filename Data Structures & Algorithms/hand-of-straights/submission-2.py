class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        chk = {}
        for i in hand:
            chk[i] = chk.get(i, 0)+1
        print(chk)

        for i in hand:
            if i not in chk:
                continue
            for j in range(i, i+groupSize):
                if j not in chk:
                    return False
                chk[j] -= 1
                if chk[j] == 0:
                    del chk[j]
        return True
