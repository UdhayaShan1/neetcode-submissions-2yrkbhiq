class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chk = {}
        mapped = {}
        for i in range(len(s)):
            to = t[i]
            if s[i] in chk and chk[s[i]] != to:
                return False
            if to in mapped and mapped[to] != s[i]:
                return False
            chk[s[i]] = to
            mapped[to] = s[i]
        return True
