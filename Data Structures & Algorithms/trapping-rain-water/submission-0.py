class Solution:
    def trap(self, height: List[int]) -> int:
        curr = 0
        for i in range(len(height)):
            if i == 0 or i == len(height)-1:
                continue
            left = -float('inf')
            right = -float('inf')
            for j in range(i-1, -1, -1):
                left = max(left, height[j])
            for j in range(i+1, len(height)):
                right = max(right, height[j])
            fill = max(0, min(left, right)-height[i])
            curr += fill
        return curr

                    

