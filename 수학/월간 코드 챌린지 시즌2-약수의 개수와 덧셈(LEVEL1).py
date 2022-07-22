def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if divide(i) % 2 == 0:
            answer += i
        else:
            answer -= i
        
    return answer

def divide(num):
    num_list = []
    for i in range(1, int(num**(1/2))+1):
        if num % i == 0:
            num_list.append(i)
            if (i**2) != num:
                num_list.append(num//i)
    return len(num_list)
                