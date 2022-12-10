import heapq
def solution(n, k, enemy):
    if k > len(enemy):
        return len(enemy)
    
    heap = enemy[:k]
    heapq.heapify(heap)
    for i in range(k, len(enemy)):
        heapq.heappush(heap, enemy[i]) 
        n -= heapq.heappop(heap) 
        if n < 0:
            return i
    return len(enemy)