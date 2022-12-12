from collections import defaultdict
def solution(fees, records):
    answer = []
    dictionary_setting = defaultdict(list)
    #각 번호판에 대한 IN, OUT 삽입
    for i in records:
        check_time = i.split(" ")
        result_time = clock(check_time[0])
        dictionary_setting[check_time[1]].append(result_time)
    dictionary = dict(sorted(dictionary_setting.items()))
    #홀수 인경우 23:59분 1439추가
    for i in dictionary:
        if len(dictionary[i]) % 2 != 0:
            dictionary[i].append(1439)
    for i in dictionary:
        result = 0
        for j in range(0,len(dictionary[i]),2):
            result += dictionary[i][j+1]-dictionary[i][j]
        answer.append(calculate(result, fees))
    
    
    return answer
#분으로 변경
def clock(value):
    check = list(map(int, value.split(":")))
    result = check[0]*60 + check[1]
    return result
#주차 요금 계산
def calculate(result, fees):
    calculate_result = fees[1]
    result -= fees[0]
    if result <= 0:
        return calculate_result
    calculate_result += (result//fees[2]) * fees[3]
    print(result)
    if result % fees[2] >0 :
        calculate_result += fees[3]
    return calculate_result
        