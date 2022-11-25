from collections import deque
import sys
read = sys.stdin.readline

n,m = map(int, read().split())

graph = [list(map(int, read().split())) for _ in range(n)]
max_answer = 0
#상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0


def bfs(graph,a,b):
    check_max_answer = 1
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
                check_max_answer += 1
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return check_max_answer
    
    

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            
            check_answer = bfs(graph,i,j)
            if max_answer < check_answer:
                max_answer = check_answer
            count += 1
print(count)
print(max_answer)
        