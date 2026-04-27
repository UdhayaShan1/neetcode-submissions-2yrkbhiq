class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = 0
        for i in range(k):
            if blocks[i] == 'W':
                w += 1
        left = 0
        right = k-1
        res = float('inf')
        while True:
            res = min(res, w)
            if right+1 >= len(blocks):
                return res
            
            if blocks[left] == 'W':
                w -= 1
            if blocks[right+1] == 'W':
                w += 1
            left += 1
            right += 1
        