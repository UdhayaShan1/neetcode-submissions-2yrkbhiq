class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        p = {}
        for i in range(len(nums)):
            if i-p.get(nums[i], -float('inf')) <= k:
                return True
            p[nums[i]] = i
        return False
        