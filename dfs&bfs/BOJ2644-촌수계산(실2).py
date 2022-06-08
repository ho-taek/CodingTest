import sys
from collections import deque

read= sys.stdin.readline
n = int(read())

x,y = map(int, read().split())

m = int(read())

relation = [ [] * (n+1) for _ in range(n+1)]
dist = [-1] * (n+1)
for i in range(m):
    a,b = map(int, read().split())
    relation[a].append(b)
    relation[b].append(a)

def bfs(x):
    queue = deque()
    queue.append(x)
    dist[x] = 0
    while queue:
        nx = queue.popleft()
        for i in relation[nx]:
           if dist[i] == -1:
               dist[i] = dist[nx] + 1
               queue.append(i)
bfs(x)
if dist[y] == -1:
    print(-1)
else:
    print(dist[y])

