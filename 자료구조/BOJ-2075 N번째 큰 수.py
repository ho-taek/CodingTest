import heapq
import sys

read = sys.stdin.readline
n = int(read())

heap = []
for i in range(n):
    num_list = list(map(int, read().rstrip().split()))
    if not heap:
        for j in num_list:
            heapq.heappush(heap, j)
    else:
        for j in num_list:
            if heap[0] < j:
                heapq.heappush(heap, j)
                heapq.heappop(heap)
print(heap[0])
