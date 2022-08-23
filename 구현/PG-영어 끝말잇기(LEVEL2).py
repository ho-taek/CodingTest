def solution(n, words):
    dic = set()
    num,check = 1,1
    answer = []
    dic.add(words[0])
    for i in range(1,len(words)):
        if num == n:
            num = 1
            check += 1
        else:
            num += 1
            
        if words[i-1][-1] != words[i][0] or words[i] in dic:
            return [num,check]
        else:
            dic.add(words[i])
        
    return [0,0]