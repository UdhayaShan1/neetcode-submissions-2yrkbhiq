class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        dead = set(deadends)
        q = deque()
        d = {}
        q.append('0000')
        d['0000'] = 0
        while q:
            curr = q.popleft()
            for j in range(len(curr)):
                aft = str((int(curr[j])+1)%10)
                bef = str((int(curr[j])-1)%10)
                new1 = curr[:j]+aft+curr[j+1:]
                new2 = curr[:j]+bef+curr[j+1:]
                if new1 not in dead and new1 not in d:
                    d[new1] = 1+d[curr]
                    q.append(new1)
                if new2 not in dead and new2 not in d:
                    d[new2] = 1+d[curr]
                    q.append(new2)
        #print(d)
        return d.get(target, -1)

