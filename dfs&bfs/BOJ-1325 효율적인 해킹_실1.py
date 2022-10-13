import sys
from collections import deque

read = sys.stdin.readline
n, m = map(int, read().split())

graph = [[] for _ in range(n+1)]

def bfs(v):
    visited = [False] * (n+1)
    queue = deque([v])
    visited[v] = True
    count = 0

    while queue:
        check = queue.popleft()
        for i in graph[check]:
            if not visited[i]:
                visited[i] = True
                count += 1
                queue.append(i)
    return count

for i in range(m):
    a,b = map(int, read().split())
    graph[b].append(a)

result = []
max_count = 0
for i in range(1,n+1):
    num = bfs(i)
    if num == max_count:
        result.append(str(i))
    if num > max_count:
        max_count = num
        result = []
        result.append(str(i))
        
print(' '.join(result))





