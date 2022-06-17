import sys
from collections import deque
read = sys.stdin.readline

n,m = map(int, read().split())
queue = deque()
queue.append((n,1))
ans = -1
while queue:
    num, count = queue.popleft()
    
    if num == m:
        ans = count
        break
    if num*2 <= m:
        queue.append((num*2, count+1))

    if int(str(num)+"1") <= m:
        queue.append((int(str(num)+"1"), count+1))

print(ans)
    
            
