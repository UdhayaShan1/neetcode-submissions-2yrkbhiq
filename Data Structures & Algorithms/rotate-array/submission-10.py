class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0 
        k = k%len(nums)
        for i in range(len(nums)):
            if count == len(nums):
                break
            curr = nums[i]
            pos = i
            remem = pos
            while True:
                
                nxt_pos = (pos+k)%len(nums)
                nxt = nums[nxt_pos]
                nums[nxt_pos] = curr
                pos = nxt_pos
                curr = nxt
                count += 1
                if pos == remem:
                    break
            #print(nums)


        