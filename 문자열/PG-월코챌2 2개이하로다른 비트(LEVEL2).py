def solution(numbers):
    answer = []
    for i in numbers:
        num = list("0"+bin(i)[2:])
        idx = "".join(num).rfind("0")
        num[idx] = '1'
        
        if i % 2 == 1:
            num[idx+1] = '0'
        answer.append(int("".join(num),2))
    return answer