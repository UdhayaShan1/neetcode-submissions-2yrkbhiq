class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        while i < len(path):
            if path[i] == '/':
                while i < len(path) and path[i] == '/':
                    i += 1
            else:
                curr = ""
                while i < len(path) and path[i] != '/':
                    curr += path[i]
                    i += 1
                if curr == '..':
                    if stack:
                        stack.pop()
                elif curr == '.':
                    pass
                else:
                    stack.append(curr)
        #print(stack)
        res = '/'
        for i in range(len(stack)):
            res += stack[i]
            if i != len(stack)-1:
                res += '/'
        return res
