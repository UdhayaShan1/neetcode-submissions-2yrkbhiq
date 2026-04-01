class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [-float('inf')]
        for i in range(1, len(height)):
            pre.append(max(height[i-1], pre[-1]))
        print(pre)

        post = [-float('inf')]
        for i in range(len(height)-2, -1, -1):
            post.append(max(height[i+1], post[-1]))
        post = post[::-1]
        print(post)

        res = 0
        for i in range(len(height)):
            res += max(0, min(pre[i], post[i]) - height[i])
        return res