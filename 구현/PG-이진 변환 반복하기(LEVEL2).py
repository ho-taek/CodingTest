def solution(s):
    zero_count,result_count = 0,0
    while s != "1":
        result_count += 1
        zero_count += s.count("0")
        s = s.replace("0","")
        num = len(s)
        s = bin(num)[2:]
        
        
    answer = [result_count,zero_count]
    return answer


