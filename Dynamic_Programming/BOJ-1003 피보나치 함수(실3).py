import sys
read = sys.stdin.readline

t = int(read())
cache = [[0,0] for i in range(41)]
cache[0]=[1,0]
cache[1]=[0,1]
def fib(n):
    if cache[n] != [0,0]:
        return cache[n]
    for i in range(2,n+1):
            cache[i][0] = cache[i-2][0] + cache[i-1][0]
            cache[i][1] = cache[i-2][1] + cache[i-1][1]
    return cache[n]

for _ in range(t):
    n = int(read())
    answer = fib(n)
    print('{} {}'.format(answer[0],answer[1]))
    
