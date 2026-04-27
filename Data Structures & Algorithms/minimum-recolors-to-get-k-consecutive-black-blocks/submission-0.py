class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        left = 0
        for i in range(k):
            if blocks[i] == 'W':
                white += 1
        right = k-1
        res = white
        while right < len(blocks):
            res = min(res, white)
            if right+1 >= len(blocks):
                break
            if blocks[left] == 'W':
                white -= 1
            if right+1 < len(blocks) and blocks[right+1] == 'W':
                white += 1
            left += 1
            right += 1
        return res

                