from collections import deque

def solution(n, computers):
    count = 0
    visited = [False] * (n)
    for i in range(n):
        if not visited[i]:
            count += 1
            bfs(i, computers, visited,n)
    return count


def bfs(start, graph, visited,n):
    queue = deque([start])
    queue.append(start)
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in range(n):
            if visited[i] == False and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True
