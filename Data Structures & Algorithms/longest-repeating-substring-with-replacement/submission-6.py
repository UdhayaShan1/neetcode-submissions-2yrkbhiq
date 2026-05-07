class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def replacements(ref):
            most = 0
            r = ""
            total = 0
            for i in ref:
                total += ref[i]
                if ref[i] > most:
                    most = ref[i]
                    r = i
            return total-most
        
        left = 0
        ref = {}
        res = 0
        for i in range(len(s)):
            ref[s[i]] = ref.get(s[i], 0)+1
            #print(ref, replacements(ref))
            while replacements(ref) > k:
                ref[s[left]] -= 1
                if ref[s[left]] == 0:
                    del ref[s[left]]
                left += 1
            res = max(res, i-left+1)
        return res
            
            

            