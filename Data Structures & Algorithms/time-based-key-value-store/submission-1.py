class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.d.get(key, []):
            return ""
        ref = self.d[key]
        s = 0
        e = len(ref)-1
        res = ""
        while s <= e:
            mid = (s+e)//2
            if ref[mid][1] > timestamp:
                e = mid-1
            else:
                res = ref[mid][0]
                s = mid+1
        return res
        
