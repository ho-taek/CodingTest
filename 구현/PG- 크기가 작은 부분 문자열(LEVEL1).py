def solution(t, p):
    answer = 0
    num = len(t)-len(p)+1
    p_num = int(p)
    for i in range(num):
        t_num = int(t[i:i+len(p)])
        if p_num >= t_num:
            answer += 1
    return answer