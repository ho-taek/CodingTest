def solution(survey, choices):
    dic = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    li = ["R","T","C","F","J","M","A","N"]
    score = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    check = -1
    while True:
        check += 1
        if check == len(survey):
            break
        if choices[check] >= 5:
            dic[survey[check][1]] += score[choices[check]]
        else:
            dic[survey[check][0]] += score[choices[check]]
    
    answer = ''
    for i in range(0,7,2):
        if dic[li[i]] >= dic[li[i+1]]:
            answer += li[i]
        else:
            answer += li[i+1]
    return answer