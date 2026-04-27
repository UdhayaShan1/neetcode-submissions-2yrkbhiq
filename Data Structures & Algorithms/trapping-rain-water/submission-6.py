class Solution:
    def trap(self, height: List[int]) -> int:
        p = [0]
        for i in range(1, len(height)):
            p.append(max(height[i-1], p[-1]))
        #print(p)

        s = [0]
        for i in range(len(height)-2, -1, -1):
            s.append(max(height[i+1], s[-1]))
        #print(s)
        s = s[::-1]

        res = 0
        for i in range(len(height)):
            res += max(min(p[i], s[i])-height[i], 0)
        return res
