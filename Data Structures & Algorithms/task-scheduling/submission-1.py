class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        class Freq:
            def __init__(self, t, freq):
                self.t = t
                self.freq = freq
            def __lt__(self, o):
                return self.freq > o.freq
        
        class Wait:
            def __init__(self, t, freq, w):
                self.t = t
                self.freq = freq
                self.w = w
            def __lt__(self, o):
                return self.w < o.w
        
        time = 0
        chk = {}
        for i in range(len(tasks)):
            chk[tasks[i]] = chk.get(tasks[i], 0)+1
        #print(chk)
        freq = []
        for i in chk:
            heapq.heappush(freq, Freq(i, chk[i]))
        wait = []

        while freq or wait:
            if freq:
                tmp = heapq.heappop(freq)
                print(tmp.t, tmp.freq, time)
                if tmp.freq > 1:
                    heapq.heappush(wait, Wait(tmp.t, tmp.freq-1, time+n+1))
                time += 1
                
                while wait and time >= wait[0].w:
                    tmp = heapq.heappop(wait)
                    heapq.heappush(freq, Freq(tmp.t, tmp.freq))
            else:
                if time < wait[0].w:
                    time = wait[0].w

                while wait and time >= wait[0].w:
                    tmp = heapq.heappop(wait)
                    heapq.heappush(freq, Freq(tmp.t, tmp.freq))
        return time
                





