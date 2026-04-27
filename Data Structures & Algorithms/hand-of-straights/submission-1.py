class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        for i in hand:
            count[i] = count.get(i, 0)+1
        
        keys = list(count.keys())
        keys.sort()

        start = 0

        i = 0
        while i < len(hand):
            while count[keys[start]] == 0:
                start += 1
            
            ref = keys[start]
            #print(start, count)
            for j in range(groupSize):
                if ref not in count or count[ref] == 0:
                    return False
                count[ref] -= 1
                ref += 1
                i += 1
        return True
