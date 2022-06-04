from collections import deque
import sys

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
read = sys.stdin.readline

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = True

    while queue:
        x,y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    queue.append((nx,ny))
                    visited[nx][ny] = True

while True:
    w,h = map(int, read().split())

    if not w and not h:
        break

    maps = [list(map(int, read().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    print(cnt)

                    
        
