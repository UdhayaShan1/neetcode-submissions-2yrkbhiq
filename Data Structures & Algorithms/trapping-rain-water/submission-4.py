class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]
        for i in range(1, len(height)):
            left.append(max(left[-1], height[i-1]))
        print(left)

        right = [0]
        for i in range(len(height)-2, -1, -1):
            right.append(max(right[-1], height[i+1]))
        right = right[::-1]
        print(right)

        res = 0
        for i in range(len(height)):
            res += max(0, min(left[i], right[i])-height[i])
        return res
