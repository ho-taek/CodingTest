from collections import deque
import sys

read = sys.stdin.readline

n = int(read())
maze = list(map(int, read().split()))

if n == 1:
    print(0)
    sys.exit()

visited = [0]*n
q = deque([(0,maze[0])])

while q:
    pos, jump = q.popleft()
    for i in range(1, jump+1):
        if pos+i >= n or visited[pos+i]:
            continue
        visited[pos+i] = visited[pos] + 1
        q.append((pos+i, maze[pos+i]))
print(visited[-1] if visited[-1]  else -1)