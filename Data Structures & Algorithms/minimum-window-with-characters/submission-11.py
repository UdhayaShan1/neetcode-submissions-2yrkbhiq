class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        t_ref = Counter(t)
        def canRemove(s, t_ref, ele):
            if ele not in t_ref:
                return True
            if s[ele] > t_ref[ele]:
                return True
            return False
        def valid(s, t):
            for i in t:
                if i not in s or s[i] < t[i]:
                    return False
            return True
        
        left = 0
        res = None
        m = float('inf')
        s_ref = Counter()
        for i in range(len(s)):
            s_ref[s[i]] += 1
            while left < len(s) and canRemove(s_ref, t_ref, s[left]):
                s_ref[s[left]] -= 1
                if s_ref[s[left]] == 0:
                    del s_ref[s[left]]
                left += 1
            if valid(s_ref, t_ref):
                l = i-left+1
                if l < m:
                    m = l
                    res = (left, i)
        if res is None:
            return ""
        return s[res[0]:res[1]+1]