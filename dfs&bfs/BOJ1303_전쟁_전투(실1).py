from collections import deque
import sys

read = sys.stdin.readline

n,m = map(int, read().split())

graph = [list(read().rstrip()) for _ in range(m)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph,a,b,color):
    white,blue = 1, 1
    queue = deque()
    queue.append((a,b))
    graph[a][b] = "G"

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if color == "white" and graph[nx][ny] == "W":
                graph[nx][ny] = "G"
                white += 1
                queue.append((nx,ny))
            
            if color == "blue" and graph[nx][ny] =="B":
                graph[nx][ny] = "G"
                blue += 1
                queue.append((nx,ny))

    return blue if color == "blue" else white

answer_white, answer_blue = 0,0

for i in range(m):
    for j in range(n):
        if graph[i][j] == "W":
            answer_count = bfs(graph,i,j,"white")
            answer_white += answer_count**2
        elif graph[i][j] == "B":
            answer_count = bfs(graph,i,j,"blue")
            answer_blue += answer_count**2

print(answer_white, answer_blue)



