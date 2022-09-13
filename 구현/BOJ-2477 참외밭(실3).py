import sys

read = sys.stdin.readline

n = int(read())
arr = [list(map(int, read().split())) for _ in range(6)]
w, index_w = 0, 0
h, index_h = 0, 0

# 가장 큰 수 및 인덱스 찾기
for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if w < arr[i][1]:
            w = arr[i][1]
            index_w = i
    else:
        if h < arr[i][1]:
            h = arr[i][1]
            index_h = i

# 넓이
subW = abs(arr[(index_w -1) % 6][1] - arr[(index_w+1)%6][1])
subH = abs(arr[(index_h-1)%6][1] - arr[(index_h+1)%6][1])
result = ((w*h)-(subW*subH)) * n
print(result)