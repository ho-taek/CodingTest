from collections import Counter
import operator as op
from functools import reduce

n = int(input())
x = [input() for _ in range(n)]


li = []
for i in x:
    cnt = 0
    for j in i:
        cnt += 1
        ans = i.replace(j,str(cnt))
        i = ans
        if cnt == len(i):
            li.append(ans)

counter = dict(Counter(li))
dictionary = list(counter.values())

def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

answer = 0
for i in dictionary:
    if i == 2:
        answer += 1
    elif i> 1:
        answer += nCr(i, 2)

print(answer)

