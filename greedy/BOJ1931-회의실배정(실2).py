import sys
N = int(sys.stdin.readline())

time = [[0]*2 for _ in range(N)]
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key = lambda x: (x[1],x[0]))
print(time)

now = time[0][1]
count= 1
for i in range(1,N):
    if now <= time[i][0]:
        count += 1
        now = time[i][1]
print(count)

