class Solution:
    def trap(self, height: List[int]) -> int:
        p = [height[0]]
        for i in range(1, len(height)):
            p.append(max(p[-1], height[i-1]))
        s = [height[-1]]
        for i in range(len(height)-2, -1, -1):
            s.append(max(s[-1], height[i+1]))
        s = s[::-1]
        print(p, s)

        res = 0
        for i in range(1, len(height)-1):
            res += max(0, min(p[i], s[i])-height[i])
        return res