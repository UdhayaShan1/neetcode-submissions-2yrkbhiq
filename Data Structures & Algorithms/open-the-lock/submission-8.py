class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if '0000' in dead:
            return -1
        start = '0000'
        d = {}
        d[start] = 0
        q = deque()
        q.append(start)

        while q:
            curr = q.popleft()
            for i in range(len(curr)):
                before = (int(curr[i])-1)%10
                after = (int(curr[i])+1)%10
                new_b = curr[:i]+str(before)+curr[i+1:]
                new_a = curr[:i]+str(after)+curr[i+1:]
                if new_b not in d and new_b not in dead:
                    d[new_b] = 1+d[curr]
                    q.append(new_b)
                if new_a not in d and new_a not in dead:
                    d[new_a] = 1+d[curr]
                    q.append(new_a)
        return d.get(target, -1)
