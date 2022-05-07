from collections import deque
import sys

read = sys.stdin.readline

n, m = map(int, read().split())

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            print(i)
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0
for _ in range(m):
    a,b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = True
        else:
            bfs(i)
            cnt += 1
print(cnt)
