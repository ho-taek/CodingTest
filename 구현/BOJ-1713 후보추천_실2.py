import sys

read = sys.stdin.readline
n = int(read())
m = int(read())
sentence = list(map(int, read().split(" ")))

answer = []
num_list = [0]*101

for i in sentence:
    # answer이 3이 아닐때
    if len(answer) != n:
        if i not in answer:
            answer.append(i)
        num_list[i] += 1
    else:
        if i not in answer:
            num_list[i] += 1
            min = 1e9
            check = 0
            for j in answer:
                if num_list[j] < min:
                    min = num_list[j]
                    check = j
            answer.remove(check)
            answer.append(i)
            num_list[check] = 0
        else:
            num_list[i] += 1
arrange = sorted(answer)
print(*arrange)