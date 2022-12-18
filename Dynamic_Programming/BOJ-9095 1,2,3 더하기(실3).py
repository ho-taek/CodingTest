import sys
read = sys.stdin.readline

n = int(read())
answer = []
def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return dp(n-3)+dp(n-2)+dp(n-1)

for i in range(n):
    m = int(read())
    print(dp(m))
