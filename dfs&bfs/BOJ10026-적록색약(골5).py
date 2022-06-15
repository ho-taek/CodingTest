import sys
from collections import deque
import copy
read = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(read().rstrip())

answer_list = [list(read().rstrip()) for _ in range(n)]
answer_list_two = copy.deepcopy(answer_list)
for i in range(n):
    for j in range(n):
        if answer_list_two[i][j] == 'G':
            answer_list_two[i][j] = 'R'

def bfs(x,y,select,num):
    queue= deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if num == 0:
                    if answer_list[nx][ny] != 0 and answer_list[nx][ny] == select:
                        queue.append([nx,ny])
                        answer_list[nx][ny] = 0
                else:
                    if answer_list_two[nx][ny] != 0 and answer_list_two[nx][ny] == select:
                        queue.append([nx,ny])
                        answer_list_two[nx][ny] = 0

count = 0
count_two = 0
for i in range(n):
    for j in range(n):
        if answer_list[i][j] != 0:
            check = answer_list[i][j]
            bfs(i,j,check,0)
            count += 1
            

for i in range(n):
    for j in range(n):
        if answer_list_two[i][j] != 0:
            check = answer_list_two[i][j]
            bfs(i,j,check,1)
            count_two += 1

print(count, count_two)


