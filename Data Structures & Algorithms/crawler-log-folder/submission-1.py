class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for i in logs:
            if i[0:2] == '..':
                level -= 1
                level = max(level, 0)
            elif i[0] != '.':
                level += 1
        return level
                