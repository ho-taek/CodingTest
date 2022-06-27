import sys
from copy import deepcopy
read = sys.stdin.readline

n = list(map(int, read().rstrip()))

li = [x for x in range(10)]
answer = deepcopy(li)

count = 1

def remove_list(x):
    global answer
    global count
    if x == 6:
        if 9 not in answer:
            count += 1
            answer = answer + li
        x = 9
    elif x == 9:
        if 6 not in answer:
            count += 1
            answer = answer + li
        x = 6
    else:
        count += 1
        answer = answer + li
    answer.remove(x)
        
for i in n:
    if i not in answer:
        remove_list(i)
    else:
        answer.remove(i)

print(count)
