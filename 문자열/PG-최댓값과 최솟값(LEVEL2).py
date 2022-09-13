def solution(s):
    num = [int(i) for i in s.split(" ")]
    num.sort()
    answer = str(num[0])+" "+str(num[-1])
    return answer