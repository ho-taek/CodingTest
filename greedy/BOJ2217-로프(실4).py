import sys
read = sys.stdin.readline

n = int(read())

rope = [int(read()) for _ in range(n)]
ans = []
rope.sort()

for i in range(n):
    num = rope[i]*(n-i)
    ans.append(num)


print(max(ans))
