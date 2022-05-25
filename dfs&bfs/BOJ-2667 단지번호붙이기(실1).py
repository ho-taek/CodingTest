from collections import deque

import sys

read = sys.stdin.readline

n = int(read())

graph = []

for _ in range(n):
    graph.append(list(map(int, read().rstrip())))

nx = [-1, 1, 0, 0]
ny = [0,0,-1,1]

def bfs(graph,x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    count = 1
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if dx < 0 or dy < 0 or dx >= n or dy >=n:
                continue
            if graph[dx][dy] == 1:
                count += 1
                graph[dx][dy] = 0
                queue.append((dx,dy))
    return count

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])




