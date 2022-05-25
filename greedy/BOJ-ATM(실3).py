import sys

read = sys.stdin.readline

n = int(read())

p = list(map(int, read().split()))

p.sort()
ans = 0
for i in range(1,n+1):
    ans += sum(p[:i])
    
print(ans)
