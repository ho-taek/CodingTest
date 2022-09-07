def solution(n):
    answer = 1
    if n == 1:
        return 1
    
    if n % 2 == 1:
        num = n//2+1
    else:
        num = n//2-1
    
    for i in range(1, num+1):
        plus = 0
        for j in range(i, num+1):
            plus += j
            if plus == n:
                answer += 1
                break
            if n < plus:
                break
    
    return answer