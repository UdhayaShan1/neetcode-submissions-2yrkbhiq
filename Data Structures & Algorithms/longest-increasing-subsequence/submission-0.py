class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ref = []
        for i in nums:
            s = 0
            e = len(ref)-1
            pos = -1
            while s <= e:
                mid = (s+e)//2
                if ref[mid] < i:
                    s = mid+1
                else:
                    pos = mid
                    e = mid-1
            print(ref, pos, i)
            if pos == -1 or pos >= len(ref):
                ref.append(i)
            else:
                ref[pos] = i
        return len(ref)



        