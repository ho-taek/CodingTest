from collections import deque

def bfs(places):
    place = []
    for i in range(5):
        for j in range(5):
            if places[i][j] == "P":
                place.append([i,j])
    
    for p in place:
        queue = deque([p])
        visited = [[0]*5 for i in range(5)]
        distance = [[0]*5 for i in range(5)]
        visited[p[0]][p[1]] = 1
    
    
        while queue:
            y,x = queue.popleft()
            
            dx = [-1,1,0,0]
            dy = [0,0,-1,1] 
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    if places[ny][nx] == 'O':
                        queue.append([ny,nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    
                    if places[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []
    for i in places:
        answer.append(bfs(i))
    
    return answer