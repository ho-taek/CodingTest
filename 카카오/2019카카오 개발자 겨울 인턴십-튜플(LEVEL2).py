def solution(s):
    answer,result,num =[],[],[]
    express = s[1:-1].split(",")
    
    for i in express:
        string = ""
        for j in i:
            if j.isdigit():
                string += j
        num.append(string)
        if "}" in i:
            result.append(num)
            num = []
    result.sort(key=len)
    for i in result:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer