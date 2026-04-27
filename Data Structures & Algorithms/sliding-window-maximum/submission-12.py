class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        maxQ = deque()
        for i in range(k):
            while maxQ and maxQ[-1][0] < nums[i]:
                maxQ.pop()
            maxQ.append((nums[i], i))
        left = 0
        right = k-1
        res = []
        while True:
            res.append(maxQ[0][0])
            if right+1 >= len(nums):
                return res
            left += 1
            while maxQ and maxQ[-1][0] < nums[right+1]:
                maxQ.pop()
            maxQ.append((nums[right+1], right+1))
            right += 1
            while maxQ and maxQ[0][-1] < left:
                maxQ.popleft()
