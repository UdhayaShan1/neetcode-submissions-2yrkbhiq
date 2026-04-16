class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ref = {}
        for i in s:
            ref[int(i)] = ref.get(int(i), 0)+1
        #print(ref)
        ref[1] -= 1
        res = "1"
        for i in range(ref.get(0, 0)):
            res += '0'
        for i in range(ref.get(1, 0)):
            res += '1'
        return res[::-1]

        