class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-1
        while left <= right:
            if right-left+1 == k:
                return arr[left:right+1]
            d1 = abs(x-arr[left])
            d2 = abs(x-arr[right])
            if d1 < d2:
                right -= 1
            elif d1 > d2:
                left += 1
            else:
                right -= 1
        
            
            