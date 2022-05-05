import sys

read = sys.stdin.readline

n = int(read())
m = int(read())


graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, read().split())
    graph[a][b] = graph[b][a] = 1

result = []
visited = [0] * (n+1)
def dfs(v):
    visited[v] = 1
    result.append(v)
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

dfs(1)
print(len(result) - 1)
    
