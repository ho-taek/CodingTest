from collections import deque
import sys

read = sys.stdin.readline

m,n,k = map(int,read().split())

graph = [ list(0 for _ in range(n)) for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int, read().split())

    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    cnt = 1

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    queue.append((ny,nx))
                    cnt += 1
    return cnt
answer = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            answer.append(bfs(i,j))
print(len(answer))
print(*sorted(answer))
    
    
