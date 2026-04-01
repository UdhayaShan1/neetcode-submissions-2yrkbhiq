class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        i = 0
        ref = ""
        while i < len(path):
            if path[i] == '/':
                i += 1
                ref = ""
                continue
            ref += path[i]
            if i+1 >= len(path) or path[i+1] == '/':
                if ref == '..':
                    if res:
                        res.pop()
                elif ref != '.':
                    res.append(ref)
            i += 1
        #print(res)
        return '/' + '/'.join(res)

