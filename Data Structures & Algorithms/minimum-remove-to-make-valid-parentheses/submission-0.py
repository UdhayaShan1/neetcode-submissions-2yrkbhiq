class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != '(' and s[i] != ')':
                continue
            stack.append((s[i], i))
            while len(stack) > 1 and stack[-1][0] == ')' and stack[-2][0] == '(':
                stack.pop()
                stack.pop()
        print(stack)
        remove = {}
        for i in stack:
            remove[i[1]] = 1
        res = ""
        for i in range(len(s)):
            if i in remove:
                continue
            res += s[i]
        return res