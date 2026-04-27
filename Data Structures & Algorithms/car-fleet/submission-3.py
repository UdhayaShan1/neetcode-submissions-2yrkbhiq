class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        class Tmp:
            def __init__(self, pos, time):
                self.pos = pos
                self.time = time
            
            def __lt__(self, o):
                return self.pos < o.pos
        
        res = []
        for i in range(len(position)):
            res.append(Tmp(position[i], (target-position[i])/speed[i]))
        
        res.sort()
        stack = []
        for i in res:
            #print(i.pos, i.time)
            stack.append(i.time)
            while len(stack) > 1 and stack[-1] >= stack[-2]:
                tmp = stack[-1]
                stack.pop()
                stack.pop()
                stack.append(tmp)


        return len(stack)
        
    