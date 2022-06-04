from collections import deque
import sys

read = sys.stdin.readline

n, m = map(int, read().split())

tomato = [list(map(int,read().split())) for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


queue = deque()
    
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            queue.append([i,j])


def bfs():    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if tomato[nx][ny] == 0:
                    queue.append([nx,ny])
                    tomato[nx][ny] = tomato[x][y] + 1
bfs()         
cnt = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))

print(cnt-1)
        
    
