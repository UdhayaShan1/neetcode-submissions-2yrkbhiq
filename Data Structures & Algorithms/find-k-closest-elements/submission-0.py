class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        class Tmp:
            def __init__(self, val):
                self.val = val
            def __lt__(self, o):
                if abs(self.val-x) != abs(o.val-x):
                    return abs(self.val-x) < abs(o.val-x)
                return self.val < o.val
        ref = []
        for i in arr:
            ref.append(Tmp(i))
        ref.sort()
        res = []
        for i in range(k):
            res.append(ref[i].val)
        res.sort()
        return res


               

                
