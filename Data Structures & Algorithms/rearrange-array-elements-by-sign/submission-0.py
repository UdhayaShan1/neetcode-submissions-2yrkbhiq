class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        
        new1 = []
        f = True
        i = 0
        j = 0
        while i < len(pos) and j < len(neg):
            if f:
                new1.append(pos[i])
                i += 1
                f = False
            else:
                new1.append(neg[j])
                j += 1
                f = True
        new1 += neg[j:]
        return new1

                