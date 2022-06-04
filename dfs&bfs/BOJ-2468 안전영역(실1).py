from collections import deque
import sys

read = sys.stdin.readline

n = int(read())

graph = [list(map(int, read().split())) for _ in range(n)]

large = max(max(graph))
ans = []


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(a,b, large):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = True

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > large:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
for k in range(0,large+1):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > k:
                bfs(i,j,k)
                cnt += 1
    
    ans.append(cnt)

print(max(ans))
                
                

        
    
        
