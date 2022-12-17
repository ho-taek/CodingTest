def solution(s):
    answer = []
    #문자열 변경 및 정렬
    dic = {}
    for i in range(1,len(s)-1):
        if s[i] == "{":
            front = i
        if s[i] == "}":
            end = i
            eng = list(map(int,s[front+1:end].split(",")))
            dic[len(eng)] = eng
    dic_sort = sorted(dic.items())
    
    #없는 값 넣기
    for i in dic_sort:
        for j in i[1]:
            if j not in answer:
                answer.append(j)
    
    return answer