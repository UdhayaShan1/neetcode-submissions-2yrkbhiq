class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]
        for i in range(1, len(height)):
            prefix.append(max(prefix[-1], height[i-1]))
        suffix = [0]
        for i in range(len(height)-2, -1, -1):
            suffix.append(max(suffix[-1], height[i+1]))
        suffix = suffix[::-1]

        print(prefix, suffix)
        res = 0
        for i in range(len(height)):
            res += max(min(prefix[i], suffix[i])-height[i], 0)
        return res