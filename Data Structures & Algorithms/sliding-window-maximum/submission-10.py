class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        for i in range(k):
            while q and nums[i] > q[-1][0]:
                q.pop()
            q.append((nums[i], i))
        
        res = []
        left = 0
        right = k-1
        while True:
            res.append(q[0][0])
            if right+1 >= len(nums):
                break
            left += 1
            while q and q[0][1] < left:
                q.popleft()
            while q and nums[right+1] > q[-1][0]:
                q.pop()
            q.append((nums[right+1], right+1))
            right += 1
        return res
