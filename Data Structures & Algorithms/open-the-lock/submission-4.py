class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from queue import Queue
        q = Queue()
        dist = {}
        q.put(("0000"))
        dist["0000"] = 1
        check = ["0", "1", "2", "3", "4", "5","6", "7","8", "9"]

        dead = {}
        for i in deadends:
            dead[i] = 1

        while not q.empty():
            curr = q.get()
            if curr in dead:
                continue
            if curr == target:
                return dist[curr]-1
            
            for i in range(4):
                nxt = check[(check.index(curr[i])+1)%len(check)]
                #print(curr, curr[i], nxt)
                new = curr[:i]+nxt+curr[i+1:]
                #print(new,'##')
                flag =  0
                if new in dead:
                    flag = 1
                if flag == 0:
                    if new not in dist:
                        dist[new] = float('inf')
                    if 1+dist[curr] < dist[new]:
                        dist[new] = 1+dist[curr]
                        q.put(new)

                nxt = check[(check.index(curr[i])-1)%len(check)]
                new = curr[:i]+nxt+curr[i+1:]

                if new in dead:
                    continue
                if new not in dist:
                    dist[new] = float('inf')
                if 1+dist[curr] < dist[new]:
                    dist[new] = 1+dist[curr]
                    q.put(new)
        return -1
        







        




        