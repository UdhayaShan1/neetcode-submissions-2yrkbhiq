class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        left = 0
        res = 0
        for i in range(len(fruits)):
            d[fruits[i]] = d.get(fruits[i], 0)+1
            while len(d) > 2:
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    del d[fruits[left]]
                left += 1
            res = max(res, i-left+1)
        return res