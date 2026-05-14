class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxQ = deque()
        res = []
        left = 0
        for i in range(len(nums)):
            while maxQ and maxQ[-1][0] < nums[i]:
                maxQ.pop()
            maxQ.append((nums[i], i))
            while i-left+1 > k:
                left += 1
                while maxQ and maxQ[0][1] < left:
                    maxQ.popleft()
            if i-left+1 == k:
                res.append(maxQ[0][0])
        return res
            