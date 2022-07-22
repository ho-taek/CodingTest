def solution(n):
    result = third(n)
    cnt = len(result)-1
    answer = 0
    for i in result:
        answer += i*(3**cnt)
        cnt -= 1
        
    return answer

def third(n):
    result = []
    while n != 0:
        result.append(n%3)
        n //= 3
    return result
        
        