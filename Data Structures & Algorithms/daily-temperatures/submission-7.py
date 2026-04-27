class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        s = []
        for i in range(len(temperatures)):
            while s and temperatures[s[-1]] < temperatures[i]:
                res[s[-1]] = i-s[-1]
                s.pop()
            s.append(i)
        return res