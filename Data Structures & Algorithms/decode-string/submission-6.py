class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        int_s = []
        while i < len(s):
            print(stack, int_s, i, s[i])
            if not s[i].isdigit():
                stack.append(s[i])
                if stack[-1] == ']':
                    ref = []
                    while True:
                        if stack[-1] == '[':
                            stack.pop()
                            hmm = int_s.pop()
                            stack += (hmm * ref[::-1])
                            break
                        if stack[-1] == ']':
                            stack.pop()
                        else:
                            ref.append(stack.pop())
                i += 1
            else:
                curr = 0
                while s[i].isdigit():
                    curr = curr*10+int(s[i])
                    i += 1
                int_s.append(curr)
        #print(stack)
        return ''.join(stack)
