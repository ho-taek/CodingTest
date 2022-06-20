import sys
from collections import deque

read = sys.stdin.readline

n,m = map(int, read().split())

check = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,read().split())
    check[b-1].append(a)
    
answer = []
def bfs(i):
    graph = [False]*n
    queue = deque([i-1])
    graph[i-1] = True
    count = 0
    while queue:
        v = queue.popleft()
        for i in check[v]:
            if graph[i-1] == False:
                graph[i-1] = True
                queue.append(i-1)
                count += 1
    return count

max_cnt = 0
for i in range(1,n+1):
    cnt = bfs(i)
    if cnt == max_cnt:
        answer.append(i)
    if cnt > max_cnt:
        max_cnt = cnt
        answer = []
        answer.append(i)
    

print(*answer)


            
            
