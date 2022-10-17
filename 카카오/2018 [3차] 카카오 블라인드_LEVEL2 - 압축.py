def solution(msg):
    dic = {}
    answer = []
    for i in range(1,27):
        dic[chr(i+64)] = i
    
    w,c = 0,0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c

    return answer
    