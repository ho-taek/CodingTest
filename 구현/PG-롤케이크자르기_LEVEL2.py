from collections import Counter

def solution(topping):
    answer = 0
    TP = Counter(topping)	
    check = set()
    for i in topping:
        TP[i] -= 1
        check.add(i)
        if TP[i] == 0:		
            TP.pop(i)
        if len(TP) == len(check):	
            answer += 1
            
    return answer