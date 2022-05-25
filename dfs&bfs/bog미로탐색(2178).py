from collections import deque

n,m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))
print(graph)
nx = [-1, 1, 0, 0]
ny = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if dx < 0 or dy <0 or dx >= n or dy >= m:
                continue
            if graph[dx][dy] == 0:
                continue
            if graph[dx][dy] == 1:
                graph[dx][dy] = graph[x][y] + 1
                queue.append((dx,dy))
    return graph[n-1][m-1]

print(bfs(0,0))
