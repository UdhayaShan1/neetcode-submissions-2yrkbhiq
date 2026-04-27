class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        chk = {}
        for i in range(len(x)):
            chk[x[i]] = max(chk.get(x[i], 0), y[i])
        #print(chk)
        ref = list(chk.values())
        ref.sort()
        if len(ref) < 3:
            return -1
        return sum(ref[-3:])