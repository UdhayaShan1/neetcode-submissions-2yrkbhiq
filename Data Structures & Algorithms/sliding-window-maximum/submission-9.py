class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        for i in range(k):
            while q and nums[i] > q[-1][1]:
                q.pop()
            q.append((i, nums[i]))
        
        res = []
        left = 0
        right = k-1
        while True:
            while q and q[0][0] < left:
                q.popleft()
            res.append(q[0][1])
            if right+1 >= len(nums):
                return res
            left += 1
            while q and nums[right+1] > q[-1][1]:
                q.pop()
            q.append((right+1, nums[right+1]))
            right += 1
        