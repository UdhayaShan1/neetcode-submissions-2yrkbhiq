class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        i = 0
        while i < len(path):
            if path[i] == '/':
                i += 1
                continue
            ref = ""
            while i < len(path) and path[i] != '/':
                ref += path[i]
                i += 1
            if ref == '..':
                if s:
                    s.pop()
            elif ref != '.':
                s.append(ref)
        return '/' + '/'.join(s)