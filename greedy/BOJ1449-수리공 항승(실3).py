N,L = map(int, input().split())

location = list(map(int, input().split()))

location.sort()
start = location[0]
count = 1

for i in location[1:]:
    if i in range(start, start+L):
        continue
    else:
        start = i
        count += 1
print(count)
