class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #print(round(6/-132))
        s = []
        for i in tokens:
            print(s)
            if i == "+":
                res = s[-2]+s[-1]
                s.pop()
                s.pop()
                s.append(res)
            elif i == "-":
                res = s[-2]-s[-1]
                s.pop()
                s.pop()
                s.append(res)
            elif i == "*":
                res = s[-2]*s[-1]
                s.pop()
                s.pop()
                s.append(res)
            elif i == "/":
                ans = s[-2]/s[-1]
                neg = ans < 0

                res = abs(s[-2])//abs(s[-1])
                if neg:
                    res = -res
                s.pop()
                s.pop()
                s.append(res)
            else:
                s.append(int(i))
        return s[-1]