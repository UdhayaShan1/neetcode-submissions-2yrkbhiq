class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums1, nums2):
            new = []
            i = 0
            j = 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    new.append(nums1[i])
                    i += 1
                else:
                    new.append(nums2[j])
                    j += 1
            while i < len(nums1):
                new.append(nums1[i])
                i += 1
            while j < len(nums2):
                new.append(nums2[j])
                j += 1
            return new

        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums)//2
            l1 = mergeSort(nums[:mid])
            l2 = mergeSort(nums[mid:])
            return merge(l1, l2)
        return mergeSort(nums)