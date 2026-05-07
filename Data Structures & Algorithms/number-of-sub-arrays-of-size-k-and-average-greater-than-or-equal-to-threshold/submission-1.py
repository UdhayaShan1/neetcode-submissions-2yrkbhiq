class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr = 0
        l = 0
        left = 0
        res = 0
        for i in range(len(arr)):
            curr += arr[i]
            l += 1
            while i-left+1 > k:
                curr -= arr[left]
                l -= 1
                left += 1
            if i-left+1 == k:
                avg = curr/l
                if avg >= threshold:
                    res += 1
        return res
