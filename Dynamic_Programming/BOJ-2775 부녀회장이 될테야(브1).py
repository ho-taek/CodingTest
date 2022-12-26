import sys
read= sys.stdin.readline

t = int(read())


answer = []
for _ in range(t):
    graph = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    k = int(read())
    n = int(read())

    if n == 1:
        print(1)
        continue
    for i in range(1,k+1):
        for j in range(1,n+1):
            graph[j] += graph[j-1]
    print(graph[n])
