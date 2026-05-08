class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = deque()
        maxQ = deque()

        def clearLeft(q, left):
            while q and q[0][1] < left:
                q.popleft()
        res = 0
        left = 0
        for i in range(len(nums)):
            while maxQ and maxQ[-1][0] < nums[i]:
                maxQ.pop()
            while minQ and minQ[-1][0] > nums[i]:
                minQ.pop()
            
            maxQ.append((nums[i], i))
            minQ.append((nums[i], i))

            while maxQ[0][0]-minQ[0][0] > limit:
                left += 1
                clearLeft(maxQ, left)
                clearLeft(minQ, left)
            res = max(res, i-left+1)
        return res
            
        
