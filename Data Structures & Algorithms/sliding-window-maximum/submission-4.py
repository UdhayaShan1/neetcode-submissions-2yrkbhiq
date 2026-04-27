class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        left = 0
        right = k-1
        for i in range(k):
            while q and q[-1][1] < nums[i]:
                q.pop()
            q.append((i, nums[i]))
        print(q)

        res = []
        while True:
            print(q, left, right)
            if q:
                res.append(q[0][1])
            if right+1 >= len(nums):
                break
            
            
            while q and nums[right+1] > q[-1][1]:
                q.pop()
            q.append((right+1, nums[right+1]))

            left += 1
            right += 1

            while q and q[0][0] < left:
                q.popleft()
        return res
