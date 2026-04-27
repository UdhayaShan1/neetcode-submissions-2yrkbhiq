class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suffix = [-1]
        for i in range(len(arr)-2, -1, -1):
            suffix.append(max(arr[i+1], suffix[-1]))
        suffix = suffix[::-1]

        return suffix