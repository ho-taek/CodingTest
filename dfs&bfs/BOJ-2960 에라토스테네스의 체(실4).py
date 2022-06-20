import sys

read= sys.stdin.readline

n,k = map(int,read().split())

graph = [ x for x in range(2,n+1)]


answer = []
count = 0
def dfs(x):
    global count
    for i in range(x,n+1,x):
        if i not in answer:
            count += 1
            answer.append(i)
        if count == k:
            print(answer[k-1])
            return
    dfs(x+1)

dfs(2)
