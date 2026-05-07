class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b = 0
        w = 0
        left = 0
        res = float('inf')
        for i in range(len(blocks)):
            if blocks[i] == 'W':
                w += 1
            else:
                b += 1
            while i-left+1 > k:
                if blocks[left] == 'W':
                    w -= 1
                else:
                    b -= 1
                left += 1
            if i-left+1 == k:
                res = min(res, w)
        return res
