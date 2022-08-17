import sys
import heapq
read = sys.stdin.readline

n = int(read())
num = [int(read()) for _ in range(n)]
heap = []
for i in num:
    if i == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-i,i))