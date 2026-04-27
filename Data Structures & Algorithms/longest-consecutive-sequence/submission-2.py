class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        prefix = [0]
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            elif nums[i] == nums[i-1]:
                prefix.append(prefix[-1])
            elif nums[i] == nums[i-1]+1:
                prefix.append(prefix[-1]+1)
            else:
                prefix.append(1)
        #print(nums, prefix)
        return max(prefix)