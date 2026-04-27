class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        chk = {}
        for i in range(len(nums)):
            if nums[i] not in chk:
                chk[nums[i]] = []
            chk[nums[i]].append(i)
            ref = chk[nums[i]]
            if len(ref) >= 2:
                if ref[-1]-ref[-2] <= k:
                    return True
        return False