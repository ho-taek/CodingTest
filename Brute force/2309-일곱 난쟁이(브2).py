from itertools import combinations

height = [int(input()) for _ in range(9)]

data = combinations(height, 7)

for i in data:
    if sum(i) == 100:
        print(*sorted(i), sep="\n")
        break
