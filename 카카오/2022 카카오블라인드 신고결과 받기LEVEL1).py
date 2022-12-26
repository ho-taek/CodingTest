from collections import defaultdict
def solution(id_list, report, k):
    report_set = list(set(report))
    user = dict.fromkeys(id_list,0)
    report = defaultdict(list)
    for i in report_set:
        x,y = i.split(" ")
        report[y].append(x)
    
    for i in report.values():
        if len(i) >= k:
            for j in i:
                user[j] += 1
    
    return list(user.values())