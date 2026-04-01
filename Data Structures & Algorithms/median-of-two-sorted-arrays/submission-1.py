class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0
        s = len(nums1)+len(nums2)
        p = s//2+1
        med1 = None
        med2 = None
        i = 0
        j = 0
        ref = 0
        while i < len(nums1) and j < len(nums2):
            if ref == p:
                break
            update = None
            if nums1[i] < nums2[j]:
                update = nums1[i]
                i += 1
            else:
                update = nums2[j]
                j += 1
            
            if med1 is None:
                med1 = update
            elif med2 is None:
                med2 = update
            else:
                med1 = med2
                med2 = update
            ref += 1
        
        if ref != p:
            while i < len(nums1):
                if ref == p:
                    break
                update = nums1[i]
                i += 1
                ref += 1

                if med1 is None:
                    med1 = update
                elif med2 is None:
                    med2 = update
                else:
                    med1 = med2
                    med2 = update
            while j < len(nums2):
                if ref == p:
                    break
                update = nums2[j]
                j += 1
                ref += 1

                if med1 is None:
                    med1 = update
                elif med2 is None:
                    med2 = update
                else:
                    med1 = med2
                    med2 = update
        print(med1, med2, p)
        if s % 2 == 0:
            return (med1+med2)/2
        return med2 if med2 else med1
