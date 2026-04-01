class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        maxQ = deque()
        for i in range(k):
            if not maxQ:
                maxQ.append((i, nums[i]))
            else:
                while maxQ and maxQ[-1][1] < nums[i]:
                    maxQ.pop()
                maxQ.append((i, nums[i]))
        print(maxQ)
        left = 0
        right = k-1
        res = []
        while True:
            #print(maxQ)
            res.append(maxQ[0][1])
            if right+1 >= len(nums):
                return res
            while maxQ and maxQ[-1][1] < nums[right+1]:
                maxQ.pop()
            maxQ.append((right+1, nums[right+1]))
            left += 1
            right += 1
            while maxQ and maxQ[0][0] < left:
                maxQ.popleft()
        return res
            
