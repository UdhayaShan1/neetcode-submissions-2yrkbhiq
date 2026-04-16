class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i = len(a)-1
        j = len(b)-1
        carry = 0
        while i >= 0 and j >= 0:
            curr = int(a[i])+int(b[j])+carry
            res.append(str(curr%2))
            if curr >= 2:
                carry = 1
            else:
                carry = 0
            i -= 1
            j -= 1
        print(res, carry)

        while i >= 0:
            curr = int(a[i])+carry
            res.append(str(curr%2))
            if curr >= 2:
                carry = 1
            else:
                carry = 0
            i -= 1
        while j >= 0:
            curr = int(b[j])+carry
            res.append(str(curr%2))
            if curr >= 2:
                carry = 1
            else:
                carry = 0
            j -= 1
        print(res)
        if carry:
            res.append("1")
        return ''.join(res[::-1])

