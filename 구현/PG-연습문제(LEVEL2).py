from collections import Counter
def solution(k, tangerine):
    count_tangerine = Counter(tangerine)
    sort_count = list(map(list,sorted(count_tangerine.items(), key=lambda x: x[1])))
    for i in range(len(tangerine) - k):
        sort_count[0][1] -= 1
        if sort_count[0][1] == 0:
            sort_count.pop(0)

    return len(sort_count)