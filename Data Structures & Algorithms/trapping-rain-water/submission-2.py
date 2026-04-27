class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_r = []
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                prefix_r.append(0)
            else:
                prefix_r.append(max(height[i+1], prefix_r[-1]))
        prefix_r = prefix_r[::-1]
        print(prefix_r)

        prefix_l = []
        for i in range(len(height)):
            if i == 0:
                prefix_l.append(0)
            else:
                prefix_l.append(max(height[i-1], prefix_l[-1]))
        print(prefix_l)
        res = 0
        for i in range(len(height)):
             max_r = prefix_r[i]
             max_l = prefix_l[i]
             res += max(0, min(max_r, max_l)-height[i])
        return res


