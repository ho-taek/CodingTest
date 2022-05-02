from itertools import combinations
from collections import deque

while True:
    s = deque(list(map(int, input().split())))
    if s[0] == 0:
        break
    s.popleft()
    s = list(combinations(s,6))
    for i in s:
        for j in i:
            print(j, end=' ')
        print()
    print()
