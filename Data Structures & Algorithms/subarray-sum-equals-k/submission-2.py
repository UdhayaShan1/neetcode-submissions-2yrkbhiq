class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p = [0]
        for i in nums:
            p.append(i+p[-1])
        #print(p)
        chk = {}
        for i in p:
            chk[i] = chk.get(i, 0)+1
        
        #for i in range(len(p)):\
        res = 0
        chk2 = {}
        for i in p:
            res += chk2.get(i-k, 0)
            chk2[i] = chk2.get(i, 0)+1
        #print(res)
        return res

        #return 1




        