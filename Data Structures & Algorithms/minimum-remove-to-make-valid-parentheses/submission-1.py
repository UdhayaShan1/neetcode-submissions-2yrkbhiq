class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        bad = {}
        stack = []
        for i in range(len(s)):
            if s[i] != ')' and s[i] != '(':
                continue
            stack.append((s[i], i))
            while len(stack) > 1 and stack[-2][0] == '(' and stack[-1][0] == ')':
                stack.pop()
                stack.pop()
        #print(stack)
        for i in stack:
            bad[i[1]] = 1
        res = ""
        for i in range(len(s)):
            if i in bad:
                continue
            res += s[i]
        return res
