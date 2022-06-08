import sys
from  collections import deque

read = sys.stdin.readline

n = int(read)
x,y = map(int, read().split())
m = int(read)

relation = [ [0] for _ in range(n) for _ in range(n)]
print(relation)
