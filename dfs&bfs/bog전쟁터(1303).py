n,m = map(int, input().split())

graph = []
ans = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x<= -1 or x >= n or y <= -1 or y >= m:
        return false
    if graph[x][y] == "Y":
            graph[x][y] = "Y"
            dfs(x-1, y):
                
