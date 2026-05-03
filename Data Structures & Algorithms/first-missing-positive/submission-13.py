class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i <= 0 or i > len(nums):
                continue
            curr = nums[i]
            pos = i
            while True:
                if curr == pos+1 or curr <= 0 or curr > len(nums):
                    break
                nxt = nums[curr-1]
                nxt_pos = curr-1
                nums[curr-1] = curr
                curr = nxt
                pos = nxt_pos
        #print(nums)
        count = 1
        for i in nums:
            if i != count:
                return count
            count += 1
        return count