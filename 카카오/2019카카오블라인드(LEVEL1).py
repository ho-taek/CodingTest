def divide(num, all):
    return num/all

def solution(N, stages):
    dict = {}
    cnt = len(stages)
    for i in range(1, N+1):
        if cnt > 0 :
            dict[i] = divide(stages.count(i), cnt)
            cnt -= stages.count(i)
        else:
            dict[i] = 0       
    answer = [x[0] for x in sorted(dict.items(), key = lambda x:x[1],
             reverse = True)]
    return answer


