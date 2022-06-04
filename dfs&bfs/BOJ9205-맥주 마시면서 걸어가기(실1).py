from collections import deque
import sys

read = sys.stdin.readline

t = int(read())
def bfs():
    queue = deque()
    queue.append(start)
    while queue:
        x,y = queue.popleft()

        if abs(x-festiv[0]) + abs(y-festiv[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = depart[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    queue.append([nx,ny])
                    visited[i] = True
    print("sad")
    return

for _ in range(t):
    n = int(read())

    start = [int(x) for x in read().split()]
    depart = [[int(x) for x in read().split()] for _ in range(n)]
    festiv = [int(x) for x  in read().split()]
    visited = [False] * (n+1)
    bfs()
    

