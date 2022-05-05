N,M = map(int, input().split())

card = list(map(int, input().split()))


result = 0
for _ in range(M):
    card.sort()
    card[0] = card[1] = card[0] + card[1]

result = sum(card)
print(result)
    
