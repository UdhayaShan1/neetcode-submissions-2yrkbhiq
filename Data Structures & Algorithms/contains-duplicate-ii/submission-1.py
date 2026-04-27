class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        chk = {}
        for i in range(len(nums)):
            ref = nums[i]
            if ref not in chk:
                chk[ref] = i
            else:
                if i-chk[ref] <= k:
                    return True
                chk[ref] = i
        return False