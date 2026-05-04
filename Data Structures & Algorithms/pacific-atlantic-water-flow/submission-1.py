class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def find(t):
            q = deque()
            d = {}
            if t == 1:
                for i in range(len(heights)):
                    for j in range(len(heights[0])):
                        if i == 0:
                            q.append((i, j))
                        elif j == 0:
                            q.append((i, j))
            else:
                for i in range(len(heights)):
                    for j in range(len(heights[0])):
                        if i == len(heights)-1:
                            q.append((i, j))
                        elif j == len(heights[0])-1:
                            q.append((i, j))
            print(q)
            for i in q:
                d[i] = 0
            
            while q:
                curr = q.popleft()
                for k in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                    new_i = curr[0]+k[0]
                    new_j = curr[1]+k[1]
                    if new_i < 0 or new_j < 0 or new_i >= len(heights) or new_j >= len(heights[0]):
                        continue
                    if (new_i, new_j) in d or heights[new_i][new_j] < heights[curr[0]][curr[1]]:
                        continue
                    d[(new_i, new_j)] = 1+d[curr]
                    q.append((new_i, new_j))
            return d


        d1 = set(find(1))
        d2 = set(find(2))
        print(d1, d2)
        return list(d1.intersection(d2))
