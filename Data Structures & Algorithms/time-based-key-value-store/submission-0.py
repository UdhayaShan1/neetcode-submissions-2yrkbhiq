class Emotion:
    def __init__(self, e, t):
        self.e = e
        self.t = t
    def __lt__(self, o):
        return self.t < o.t

class TimeMap:

    def __init__(self):
        self.ref = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ref:
            self.ref[key] = []
        self.ref[key].append(Emotion(value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        chk = self.ref.get(key, [])
        start = 0
        end = len(chk)-1
        res = -1
        while start <= end:
            mid = (start+end)//2
            if chk[mid].t <= timestamp:
                res = max(res, mid)
                start = mid+1
            else:
                end = mid-1
        if res == -1:
            return ""
        return chk[res].e

        
