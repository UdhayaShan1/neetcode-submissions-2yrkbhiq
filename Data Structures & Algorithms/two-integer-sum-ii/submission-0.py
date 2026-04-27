class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        res = []
        while i < j:
            ref = numbers[i]+numbers[j]
            if ref == target:
                return [i+1, j+1]
            if ref < target:
                i += 1
            else:
                j -= 1
        
