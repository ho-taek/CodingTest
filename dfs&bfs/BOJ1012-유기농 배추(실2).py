from collections import deque
import sys

read = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0, 0,1,-1]


t = int(read())

def bfs(graph,a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))

for _ in range(t):

    n,m,k = map(int, read().split())
    graph = [[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        a,b = map(int, read().split())
        graph[a][b] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph,a,b)
                cnt += 1
    print(cnt)
