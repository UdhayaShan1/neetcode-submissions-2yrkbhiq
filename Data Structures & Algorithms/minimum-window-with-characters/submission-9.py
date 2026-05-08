class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ref_t = {}
        for i in t:
            ref_t[i] = ref_t.get(i, 0)+1
        

        def canRemove(ref, chk):
            if chk not in ref_t or ref[chk] > ref_t[chk]:
                return True
            return False
        
        def valid(ref):
            for i in ref_t:
                if i not in ref:
                    return False
                if ref[i] < ref_t[i]:
                    return False
            return True

        left = 0
        ref = {}
        best = float('inf')
        res = None
        for i in range(len(s)):
            ref[s[i]] = ref.get(s[i], 0)+1
            while left < i and canRemove(ref, s[left]):
                #print(ref, s[left], left, i)
                ref[s[left]] -= 1
                if ref[s[left]] == 0:
                    del ref[s[left]]
                left += 1
            if valid(ref):
                if i-left+1 < best:
                    best = i-left+1
                    res = (left, i)
                #print(left, i, s[left:i+1])
        if res is None:
            return ''
        return s[res[0]:res[1]+1]
