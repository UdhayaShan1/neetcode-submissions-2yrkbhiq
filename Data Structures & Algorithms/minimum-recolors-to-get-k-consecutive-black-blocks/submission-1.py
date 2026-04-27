class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = 0
        for i in range(k):
            if blocks[i] == 'W':
                w += 1
        left = 0
        right = k-1
        res = w
        while right < len(blocks):
            res = min(w, res)
            if right + 1 >= len(blocks):
                break
            if blocks[left] == 'W':
                w -= 1
            if blocks[right+1] == 'W':
                w += 1
            left += 1
            right += 1
        return res
            