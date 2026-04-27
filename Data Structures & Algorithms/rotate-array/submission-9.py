class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        chk = 0
        for i in range(len(nums)):
            if chk >= n:
                break
            s = i
            og = nums[i]
            while True:
                nxt = nums[(s+k)%n]
                nums[(s+k)%n] = og
                og = nxt
                s = (s+k)%n
                chk += 1
                if s == i:
                    break
            #print(nums)

        