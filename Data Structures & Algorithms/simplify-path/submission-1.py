class Solution:
    def simplifyPath(self, path: str) -> str:
        i = 0
        res = []
        while i < len(path):
            if path[i] == "/":
                i += 1
                continue
            
            chk = ""
            while i < len(path) and path[i] != '/':
                chk += path[i]
                i += 1
            
            if chk == '..':
                if len(res) > 0:
                    res.pop()
            elif chk == '.':
                pass
            else:
                res.append(chk)
        return "/" + "/".join(res)

            

            
            

            