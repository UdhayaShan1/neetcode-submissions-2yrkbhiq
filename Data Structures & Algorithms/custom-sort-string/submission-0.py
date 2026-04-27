class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        for i in order:
            tmp = ""
            for j in s:
                if j == i:
                    res += j
                else:
                    tmp += j
            s = tmp
        return res+s