class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        total = 0
        best = float('inf')
        ref = None
        for i in range(len(arr)):
            total += abs(arr[i]-x)
            while i-left+1 > k:
                total -= abs(arr[left]-x)
                left += 1
            if i-left+1 == k:
                if total < best:
                    best = total
                    ref = (left, i)
        print(best, ref)

        return arr[ref[0]:ref[1]+1]

