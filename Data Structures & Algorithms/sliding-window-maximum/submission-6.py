class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for i in range(k):
            while q and q[-1][0] < nums[i]:
                q.pop()
            q.append((nums[i], i))
        
        left = 0
        right = k-1
        res = []
        while True:
            if q:
                res.append(q[0][0])
            if right+1 >= len(nums):
                return res
            left += 1
            while q and q[0][1] < left:
                q.popleft()
            while q and q[-1][0] < nums[right+1]:
                q.pop()
            q.append((nums[right+1], right+1))
            right += 1
        return res

            