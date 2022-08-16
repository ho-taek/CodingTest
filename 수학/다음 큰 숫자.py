def solution(n):
    n_count = bin(n).count("1")
    answer = n
    while True:
        answer += 1
        if bin(answer).count("1") == n_count:
            break
    
    return answer