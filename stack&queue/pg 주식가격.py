from collections import deque

def solution(prices):
    q = deque(prices)
    answer = []
    
    while q:
        a = q.popleft()
        count = 0
        for i in q:
            count += 1
            if a > i:
                break
        answer.append(count) 
    return answer
