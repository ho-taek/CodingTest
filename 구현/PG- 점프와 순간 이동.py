def solution(n):
    ans = 0
    
    while True:
        if n == 0:
            break
        if n%2 != 0:
            ans += 1
            n -= 1
        else:
            n /= 2

    return ans