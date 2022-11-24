from collections import Counter

def solution(want, number, discount):
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    answer = 0
    for i in range(len(discount)-9):
        
        check_discount = discount[i:i+10]
        check_dic = Counter(check_discount)
        if sorted(dic.items()) == sorted(check_dic.items()):
            answer += 1
    
    return answer