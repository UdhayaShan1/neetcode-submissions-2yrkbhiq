class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for i in s:
            if i == ")":
                if len(arr) == 0 or arr[-1] != "(":
                    return False
                if len(arr) > 0:
                    arr.pop()
            elif i == "}":
                if len(arr) == 0 or arr[-1] != "{":
                    return False
                if len(arr) > 0:
                    arr.pop()
            elif i == "]":
                if len(arr) == 0 or arr[-1] != "[":
                    return False
                if len(arr) > 0:
                    arr.pop()
            else:
                arr.append(i)
        return True if len(arr) == 0 else False