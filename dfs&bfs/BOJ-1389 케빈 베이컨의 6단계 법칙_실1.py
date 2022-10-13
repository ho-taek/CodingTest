import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [[] for _ in range(n+1)]

def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        target = queue.popleft()

        for i in graph[target]:
            if not visited[i]:
                visited[i] = visited[target] + 1
                queue.append(i)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

li = []

for i in range(1, n+1):
    visited = [0] * (n+1)
    bfs(i)
    li.append(sum(visited))

print(li.index(min(li))+1)
                

