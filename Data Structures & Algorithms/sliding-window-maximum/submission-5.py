class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for i in range(k):
            while q and nums[i] > q[-1][0]:
                q.pop()
            q.append((nums[i], i))
            
        left = 0
        right = k-1
        #print(q)

        res = []
        while True:
            #print(left, right, q)
            res.append(q[0][0])
            if right+1 >= len(nums):
                return res
            
            while q and nums[right+1] > q[-1][0]:
                q.pop()
            q.append((nums[right+1], right+1))
            left += 1
            right += 1
            while q and q[0][1] < left:
                q.popleft()
        #return res
            
