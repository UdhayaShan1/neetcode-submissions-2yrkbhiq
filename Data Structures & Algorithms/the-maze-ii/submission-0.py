class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        dist = {}
        from collections import deque
        q = deque()
        ref = (start[0], start[1], None)
        dist[ref] = 0
        q.append(ref)

        while q:
            curr = q.popleft()
            #print('curr', curr)
            curr_i = curr[0]
            curr_j = curr[1]
            if curr[2]:
                if curr[2] == 'L' and ((curr_j-1 >= 0 and maze[curr_i][curr_j-1] == 1) or curr_j == 0):
                    new = (curr_i, curr_j, None)
                    if dist[curr] < dist.get(new, float('inf')):
                        dist[new] = dist[curr]
                        q.append(new)
                elif curr[2] == 'L' and curr_j-1 >= 0 and maze[curr_i][curr_j-1] == 0:
                    new = (curr_i, curr_j-1, 'L')
                    if 1+dist[curr] < dist.get(new, float('inf')):
                        dist[new] = 1+dist[curr]
                        q.append(new)
                
                if curr[2] == 'R' and ((curr_j+1 < len(maze[0]) and maze[curr_i][curr_j+1] == 1) or curr_j == len(maze[0])-1):
                    new = (curr_i, curr_j, None)
                    if dist[curr] < dist.get(new, float('inf')):
                        dist[new] = dist[curr]
                        q.append(new)
                elif curr[2] == 'R' and curr_j+1 < len(maze[0]) and maze[curr_i][curr_j+1] == 0:
                    new = (curr_i, curr_j+1, 'R')
                    if 1+dist[curr] < dist.get(new, float('inf')):
                        dist[new] = 1+dist[curr]
                        q.append(new)
                #print(curr_i, curr_j, curr[2])
                if curr[2] == 'D' and ((curr_i+1 < len(maze) and maze[curr_i+1][curr_j] == 1) or curr_i == len(maze)-1):
                    #print('@@')
                    new = (curr_i, curr_j, None)
                    if dist[curr] < dist.get(new, float('inf')):
                        dist[new] = dist[curr]
                        q.append(new)
                elif curr[2] == 'D' and curr_i+1 < len(maze) and maze[curr_i+1][curr_j] == 0:
                    #print('@@@')
                    new = (curr_i+1, curr_j, 'D')
                    if 1+dist[curr] < dist.get(new, float('inf')):
                        dist[new] = 1+dist[curr]
                        q.append(new)
                
                if curr[2] == 'U' and ((curr_i-1 >= 0 and maze[curr_i-1][curr_j] == 1) or curr_i == 0):
                    new = (curr_i, curr_j, None)
                    if dist[curr] < dist.get(new, float('inf')):
                        dist[new] = dist[curr]
                        q.append(new)
                elif curr[2] == 'U' and curr_i-1 >= 0 and maze[curr_i-1][curr_j] == 0:
                    new = (curr_i-1, curr_j, 'U')
                    if 1+dist[curr] < dist.get(new, float('inf')):
                        dist[new] = 1+dist[curr]
                        q.append(new)
            else:
                for d in ['U', 'D', 'L', 'R']:
                    new = (curr_i, curr_j, d)
                    if dist[curr] < dist.get(new, float('inf')):
                        dist[new] = dist[curr]
                        
                        q.append(new)
        #print(dist)
        res = float('inf')
        for i in dist:
            if i[0] == destination[0] and i[1] == destination[1] and i[2] is None:
                res = min(res, dist[i])
                #print(i)
        return res if res != float('inf') else -1
                
            

                
