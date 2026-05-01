class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxQ = deque()
        for i in range(k):
            while maxQ and maxQ[-1][1] < nums[i]:
                maxQ.pop()
            maxQ.append((i, nums[i]))
        
        res = []
        left = 0
        right = k-1
        while True:
            res.append(maxQ[0][1])
            if right+1 >= len(nums):
                return res
            left += 1
            while maxQ and maxQ[0][0] < left:
                maxQ.popleft()
            while maxQ and maxQ[-1][1] < nums[right+1]:
                maxQ.pop()
            maxQ.append((right+1, nums[right+1]))
            right += 1
        
        