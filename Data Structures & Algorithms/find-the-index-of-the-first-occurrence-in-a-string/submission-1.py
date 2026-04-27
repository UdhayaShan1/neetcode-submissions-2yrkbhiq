class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] != needle[0]:
                i += 1
                j = 0
            else:
                start = i
                found = True
                j = 0
                while j < len(needle):
                    if i >= len(haystack):
                        found = False
                        break
                    if haystack[i] == needle[j]:
                        i += 1
                        j += 1
                    else:
                        found = False
                        break
                if found:
                    return start
                i = start+1
                j = 0
        return -1
