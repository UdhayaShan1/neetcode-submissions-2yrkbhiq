class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        chk = {}
        left = 0
        res = 0
        for i in range(len(fruits)):
            chk[fruits[i]] = chk.get(fruits[i], 0)+1

            while len(chk) > 2:
                chk[fruits[left]] -= 1
                if chk[fruits[left]] == 0:
                    del chk[fruits[left]]
                left += 1
            res = max(res, i-left+1)
            
        return res
