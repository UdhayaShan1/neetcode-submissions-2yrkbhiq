class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ref = ""
        res = ""
        for i in str1:
            ref += i
            if len(str1) % len(ref) != 0 or len(str2) % len(ref) != 0:
                continue
            f1 = len(str1)//len(ref)
            f2 = len(str2)//len(ref)
            if f1*ref == str1 and f2*ref == str2:
                res = ref
        return res