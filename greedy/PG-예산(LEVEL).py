def solution(d, budget):
    sort = sorted(d)
    result = 0
    for i in sort:
        budget -= i
        if budget < 0:
            return result
        else:
            result += 1
        
    return result