from collections import deque
def solution(cards):
    result = []
    for i in cards:
        if max(cards) == 0:
            result.append(0)
            break
        if i != 0:
            queue = deque()
            queue.append(i)
            check = 0
            while queue:
                node = queue.popleft()
                if cards[node-1] != 0:
                    queue.append(cards[node-1])
                    cards[node-1] = 0
                    check += 1
            result.append(check)
    result.sort(reverse = True)
    answer = result[0]*result[1]
    return answer

