def solution(price, money, count):
    answer = -1
    wallet = 0
    for i in range(1,count+1):
        wallet += price*i
    
    answer = wallet-money
    if answer > 0:
        return answer
    else:
        return 0
    