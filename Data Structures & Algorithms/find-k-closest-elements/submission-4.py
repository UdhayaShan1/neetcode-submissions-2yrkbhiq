class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        curr = 0
        left = 0
        best = float('inf')
        res = None
        for i in range(len(arr)):
            curr += abs(arr[i]-x)
            while i-left+1 > k:
                curr -= abs(arr[left]-x)
                left += 1
            if i-left+1 == k:
                if curr < best:
                    best = curr
                    res = (left, i)
        #print(res)
        return arr[res[0]:res[1]+1]


            