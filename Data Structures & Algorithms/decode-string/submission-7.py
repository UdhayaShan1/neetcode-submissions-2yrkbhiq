class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s):
            #print("fuck", s)
            if len(s) <= 1:
                return s
            if 'a' <= s[0] <= 'z':
                return s[0] + dfs(s[1:])
            
            no = 0
            i = 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    no = no*10+int(s[i])
                    i += 1
                else:
                    break
            s1 = [s[i]]
            after = -1
            ref = "["
            i += 1
            for i in range(i, len(s)):
                ref += s[i]
                #print('@', ref, s1)
                if s[i] == ']':
                    after = i
                    s1.pop() 
                elif s[i] == '[':
                    s1.append(s[i])
                if not s1:
                    break
            #print(s, ref, after)
            return no*dfs(ref[1:-1]) + dfs(s[after+1:])
        return dfs(s)