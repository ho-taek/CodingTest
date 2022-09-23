from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for i in cities:
        i = i.upper()
        if cacheSize == 0:
            answer = len(cities)*5
            break
        
        if len(cache) < cacheSize:
            if i in cache:
                cache.remove(i)
                answer += 1
            else:
                answer += 5
            cache.append(i)
        else:
            if i in cache:
                cache.remove(i)
                answer += 1
            else:
                cache.popleft()
                answer += 5
            cache.append(i)
    return answer