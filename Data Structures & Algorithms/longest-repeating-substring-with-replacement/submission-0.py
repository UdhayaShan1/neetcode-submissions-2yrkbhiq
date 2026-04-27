class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr = {}
        def invalid(curr):
            ref = ""
            sofar = -float('inf')
            for i in curr:
                if curr[i] > sofar:
                    sofar = curr[i]
                    ref = i
            count = 0
            for i in curr:
                if curr[i] > 0 and i != ref:
                    count += curr[i]
            return count > k

 



        left = 0
        res = 1
        for i in range(len(s)):
            if s[i] not in curr:
                curr[s[i]] = 0
            curr[s[i]] += 1

            while invalid(curr):
                curr[s[left]] -= 1
                left += 1
            res = max(res, i-left+1)
        return res
            
            


