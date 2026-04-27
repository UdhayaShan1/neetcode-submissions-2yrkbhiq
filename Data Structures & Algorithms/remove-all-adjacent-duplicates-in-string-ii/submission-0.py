class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        arr = []
        i = 0
        while i < len(s):
            ref = s[i]
            count = 0
            while i < len(s) and s[i] == ref:
                count += 1
                i += 1
            arr.append((ref, count))
        #print(arr)
        stack = []
        for i in arr:
            stack.append(i)
            while stack:
                if len(stack) > 1 and stack[-2][0] == stack[-1][0]:
                    ref = stack[-2][0]
                    total = stack[-2][1]+stack[-1][1]
                    stack.pop()
                    stack.pop()
                    stack.append((ref, total))
                elif stack[-1][1] >= k:
                    ref = stack.pop()
                    if ref[1] % k != 0:
                        stack.append((ref[0], ref[1]%k))
                else:
                    break
        new = ""
        for i in stack:
            new += (i[0]*i[1])
        return new