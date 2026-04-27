class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i]+prefix[-1])
        for i in range(len(prefix)):
            prefix[i] %= k
        
        #print(prefix)
        chk = {}
        chk[0] = -1
        for i in range(len(prefix)):
            if prefix[i] in chk and i-chk[prefix[i]] >= 2:
                return True
            if prefix[i] not in chk:
                chk[prefix[i]] = i
        return False