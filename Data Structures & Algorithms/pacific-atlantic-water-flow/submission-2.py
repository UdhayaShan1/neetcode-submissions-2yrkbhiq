class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def get_d(s):
            q = deque()
            d = {}
            if s == "P":
                for col in range(len(heights[0])):
                    q.append((0, col))
                    d[(0, col)] = 0
                for row in range(1, len(heights)):
                    q.append((row, 0))
                    d[(row, 0)] = 0
            else:
                for col in range(len(heights[0])):
                    q.append((len(heights)-1, col))
                    d[(len(heights)-1, col)] = 0
                for row in range(len(heights)-2, -1, -1):
                    q.append((row, len(heights[0])-1))
                    d[(row, len(heights[0])-1)] = 0
            #print(d)
            while q:
                curr = q.popleft()
                for k in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_i = curr[0]+k[0]
                    new_j = curr[1]+k[1]
                    ref = (new_i, new_j)
                    if new_i < 0 or new_j < 0 or new_i >= len(heights) or new_j >= len(heights[0]) or ref in d:
                        continue
                    if heights[new_i][new_j] < heights[curr[0]][curr[1]]:
                        continue
                    d[ref] = 1+d[curr]
                    q.append(ref)
            print(d)
            return d
        
        d1=  get_d("P")
        d2 = get_d("A")
        res = []
        for i in d1:
            if i in d2:
                res.append(list(i))
        return res