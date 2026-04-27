class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if 1 <= nums[i] <= len(nums):
                pos = i
                curr = nums[pos]
                while True:
                    print(nums)
                    if curr == pos+1 or curr < 1 or curr > len(nums):
                        break
                    nxt = nums[curr-1]
                    nums[curr-1] = curr
                    pos = curr-1
                    curr = nxt
                    
        find = 1
        for i in nums:
            if i != find:
                return find
            find += 1
        return find
