import sys

n,m = map(int,sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree)

answer = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in tree:
        if i > mid:
            total += i - mid

    if total < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1
    
print(answer)       
    
     



