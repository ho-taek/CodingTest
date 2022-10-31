import sys

read = sys.stdin.readline

n,m = map(int, read().split())

min_num = min(n,m)
max_num = max(n,m)

graph = [list(read().rstrip()) for _ in range(n)]


def check(graph,min_num,max_num):
    for i in range(min_num,1,-1):
        
        

print(check(graph,min_num,max_num))





