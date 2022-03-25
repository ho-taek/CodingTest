n = int(input())

rank = [int(input()) for _ in range(n)]

rank.sort()
answer = 0

for x,y in enumerate(rank):
    if x+1!=y :
        answer += abs(x+1 - y)

print(str(answer))

