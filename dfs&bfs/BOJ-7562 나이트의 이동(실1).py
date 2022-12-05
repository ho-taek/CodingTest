from collections import deque
import sys

read= sys.stdin.readline
test = int(read())
dx = [-1,-2,1,2,-2,-1,2,1]
dy = [-2,-1,-2,-1,1,2,1,2]



def bfs(graph,start,end):
    if start == end:
        return 0
    queue = deque()
    queue.append((start[0],start[1]))
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
    return graph[end[0]][end[1]]
answer = []
for i in range(test):
    n = int(read())
    start = list(map(int, read().rstrip().split()))
    end = list(map(int, read().rstrip().split()))
    graph = [[0]*n for _ in range(n)]
    answer.append(bfs(graph,start,end))

print(*answer, sep='\n')