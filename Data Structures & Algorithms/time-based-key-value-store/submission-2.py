class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if len(self.map.get(key, [])) == 0:
            return ""
        s = 0
        ref = self.map[key]
        print(ref)
        e = len(ref)-1
        r = ""
        while s <= e:
            mid = (s+e)//2
            if ref[mid][1] > timestamp:
                e = mid-1
            else:
                r = ref[mid][0]
                s = mid+1
        return r

        
