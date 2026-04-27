class Solution:
    def decodeString(self, s: str) -> str:
        nums = "0123456789"
        alpha = "abcdefghijklmnopqrstuvwxyz"
        def dfs(str1):
            end = False
            for i in str1:
                if i not in alpha:
                    end = True
            if not end:
                return str1
            #print(str1)
            if len(str1) <= 1:
                return str1
            

            y1 = ""
            i = 0
            curr = ""
            ref = 0
            while i < len(str1):
                if str1[i] in alpha:
                    while i < len(str1) and str1[i] in alpha:
                        curr += str1[i]
                        i += 1
                    #print(curr)
                    y1 += dfs(curr)
                    ref = 0
                    
                elif str1[i] in nums:
                    #y1 += dfs(curr)
                    #print(curr, "@@@")
                    ref = ref*10+int(str1[i])
                    i += 1
                else:
                    stack = [('[', i)]
                    
                    i += 1
                    start = i
                    #print(start, 'hmm')
                    last = -1
                    while i < len(str1):
                        if str1[i] == '[':
                            stack.append([('(', i)])
                        elif str1[i] == ']':
                            stack.pop()
                            if len(stack) == 0:
                                last = i
                                break
                        i += 1
                    
                    i = last+1
                    #print(start, last, ref, i, "@", str1)
                    y1 += ref*dfs(str1[start:last])
                    ref = 0
                    curr = ""
            return y1
        return dfs(s)
                    
                            






