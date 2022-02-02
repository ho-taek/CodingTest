def solution(answers):
    person = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    answer = [0,0,0]
    ans = []
    for i in range(len(person)):
        for j in range(len(answers)):
            x = len(person[i])
            if answers[j] == person[i][j%x]:
                answer[i] += 1
                
    for idx,score in enumerate(answer):
        if score == max(answer):
            ans.append(idx+1)
    
    return ans
