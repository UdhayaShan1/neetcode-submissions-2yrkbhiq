class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            arr3 = []
            i = 0
            j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    arr3.append(arr1[i])
                    i += 1
                else:
                    arr3.append(arr2[j])
                    j += 1
            arr3.extend(arr1[i:])
            arr3.extend(arr2[j:])
            return arr3
        
        def mergeS(i, j):
            if i == j:
                return nums[i:j+1]
            if i > j:
                return []
            
            mid = (i+j)//2
            arr1 = mergeS(i, mid)
            arr2 = mergeS(mid+1, j)
            return merge(arr1, arr2)
        return mergeS(0, len(nums)-1)