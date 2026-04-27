class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr = 0
        res = 0
        for i in range(k):
            curr += arr[i]
        left = 0
        right = k-1
        while True:
            if curr/k >= threshold:
                res += 1
            if right+1 >= len(arr):
                return res
            curr -= arr[left]
            curr += arr[right+1]
            left += 1
            right += 1
        