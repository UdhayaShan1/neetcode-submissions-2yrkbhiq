class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        class Tmp:
            def __init__(self, u, t, w):
                self.u = u
                self.t = t
                self.w = w
            def __lt__(self, o):
                return self.t < o.t
        

        ref = []
        for i in range(len(username)):
            ref.append(Tmp(username[i], timestamp[i], website[i]))
        ref.sort()

        chk = {}
        for i in ref:
            u = i.u
            t = i.t
            w = i.w
            if u not in chk:
                chk[u] = []
            
            chk[u].append(w)

        #print(chk)

        patterns = {}
        for i in chk:
            ref = chk[i]
            for j in range(len(ref)):
                tmp = tuple(ref[j:j+3])
                if len(tmp) != 3:
                    break
                patterns[tmp] = patterns.get(tmp, 0)+1
        #print(patterns)


        class Tmp2:
            def __init__(self, t, freq):
                self.t = t
                self.freq = freq
            def __lt__(self, o):
                if self.freq != o.freq:
                    return self.freq > o.freq
                ref1 = ' '.join(list(self.t))
                ref2 = ' '.join(list(o.t))
                return ref1 < ref2
        
        new = []
        for i in patterns:
            new.append(Tmp2(i, patterns[i]))
        new.sort()

        return list(new[0].t)
                