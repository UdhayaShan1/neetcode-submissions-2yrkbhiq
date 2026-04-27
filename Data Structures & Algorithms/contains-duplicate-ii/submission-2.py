class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        chk = {}
        for i in range(len(nums)):
            ref = nums[i]
            if ref not in chk:
                chk[ref] = []
            chk[ref].append(i)
            if len(chk[ref]) > 1:
                if chk[ref][-1]-chk[ref][-2] <= k:
                    return True
        return False