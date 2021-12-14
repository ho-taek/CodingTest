def solution(brown, yellow):

    s = brown + yellow
    answer = [0, 0]
    
    for i in range(3,s):
        if  s % i  == 0 :
            height = s // i
            y = (i-2) * (height - 2)
            b = s - y
            if (brown == b and yellow == y):
                answer[0] = i
                answer[1] = height
        
    return answer
