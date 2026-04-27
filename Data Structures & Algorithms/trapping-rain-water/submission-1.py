class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_r = [0]
        for i in range(len(height)-1, -1, -1):
            prefix_r.append(max(height[i], prefix_r[-1]))
        prefix_r = prefix_r[::-1]
        print(prefix_r)

        prefix_l = [0]
        for i in range(len(height)):
            prefix_l.append(max(height[i], prefix_l[-1]))
        print(prefix_l)
        res = 0
        for i in range(len(height)):
             max_r = prefix_r[i+1]
             max_l = prefix_l[i]
             res += max(0, min(max_r, max_l)-height[i])
        return res


