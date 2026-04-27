class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d_t = {}
        for i in t:
            d_t[i] = d_t.get(i, 0)+1
        print(d_t)
        def canRemove(d, ref):
            if ref not in d_t or d[ref]-1 >= d_t[ref]:
                return True
            return False
        def valid(d):
            for i in d_t:
                if i not in d or d[i] < d_t[i]:
                    return False
            return True
        
        d = {}
        left = 0
        res = float('inf')
        ans = None
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0)+1
            while left <= i and canRemove(d, s[left]):
                #print(d)
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left += 1
            if valid(d) and (i-left+1 < res):
                res = i-left+1
                ans = (left, i)
        if not ans:
            return ""
        return s[ans[0]:ans[1]+1]