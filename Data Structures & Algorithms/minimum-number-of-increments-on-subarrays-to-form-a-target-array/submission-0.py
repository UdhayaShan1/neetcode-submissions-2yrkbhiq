class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ref = [target[0]]
        for i in range(1, len(target)):
            if target[i] <= target[i-1]:
                ref.append(0)
            else:
                ref.append(target[i]-target[i-1])
        return sum(ref)