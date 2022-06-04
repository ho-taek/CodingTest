from collections import deque
import sys

read = sys.stdin.readline

n,k = map(int, read().split())

length = 10 ** 5
dx = [0] * (length+1)

def bfs():
    q = deque([n])
    while q:
        v = q.popleft()
        if v == k:
            print(dx[k])
            break
        for nx in (v+1, v-1, v*2):
            if 0 <= nx <= length and not dx[nx]:
                q.append(nx)
                dx[nx] = dx[v] + 1
bfs()
