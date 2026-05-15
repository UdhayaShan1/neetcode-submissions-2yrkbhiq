class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)
        from functools import cache
        @cache
        def stone(alice, i, j):
            if i > j:
                return 0
            if alice:
                return max(stone(not alice, i+1, j)+piles[i], stone(not alice, i, j-1)+piles[j])
            return min(stone(not alice, i+1, j), stone(not alice, i, j-1))
        
        ref = stone(True, 0, len(piles)-1)
        return ref > total-ref
        