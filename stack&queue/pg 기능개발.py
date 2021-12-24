import math

def solution(progresses, speeds):
    day = []
    count = 1
    answer = [ ]
    for i in range(len(progresses)):
        rest = (100-progresses[i])/speeds[i]
        day.append(math.ceil(rest))

    while day:
        count = 1
        if len(day) == 1:
            break
        a = day[0]
        day.pop(0)
        while day:
            b = day[0]
            if a < b :
                answer.append(count)
                break
            day.pop(0)
            count += 1
    
    answer.append(count)
    return answer
            

