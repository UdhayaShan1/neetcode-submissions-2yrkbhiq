class Solution:
    def trap(self, height: List[int]) -> int:
        pl = [-float('inf')]
        pr = [-float('inf')]
        for i in range(1, len(height)):
            pl.append(max(pl[-1], height[i-1]))
        print(pl)

        for i in range(len(height)-2, -1, -1):
            pr.append(max(pr[-1], height[i+1]))
        pr = pr[::-1]
        print(pr)
        res = 0
        for i in range(1, len(height)-1):
            res += max(0, min(pl[i], pr[i])-height[i])
        return res


