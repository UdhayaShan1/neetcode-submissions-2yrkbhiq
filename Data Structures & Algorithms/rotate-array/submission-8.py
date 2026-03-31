class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        k %= len(nums)
        count = 0
        for i in range(len(nums)):
            if count >= len(nums):
                break
            start = i
            r = nums[start]
            while True:
                nxt = nums[(start+k)%len(nums)]
                nums[(start+k)%len(nums)] = r
                start = (start+k)%len(nums)
                r = nxt
                count += 1
                if start == i:
                    break
            print(nums)
        


        