from collections import defaultdict
def solution(id_list, report, k):
    report = list(set(report))
    cnt = defaultdict(int)
    user = defaultdict(set)
    answer =[]
    for i in report:
        a,b = i.split()
        user[a].add(b)
        cnt[b] += 1
    
    for i in id_list:
        result = 0
        for u in user[i]:
            if cnt[u] >=k:
                result += 1
        answer.append(result)
    
    return answer
