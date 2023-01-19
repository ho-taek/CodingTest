from collections import deque
import copy
def solution(n, wires):
    if n == 2:
        return 0
    answer = 1e9
    tree = list([] for _ in range(n+1))
    index = 0
    
    for x,y in wires:
        tree[x].append(y)
        tree[y].append(x)
    
    
    while index != n-1:
        visited = [True]+[False]*(n)
        tree_copy = copy.deepcopy(tree)
        x,y = wires[index]
        tree_copy[x].remove(y)
        tree_copy[y].remove(x)
        
        first_count = 0
        for i in range(1,n+1):
            if tree_copy[i]:
                first_count = bfs(i,visited,tree_copy)
                break
        
        
        second_count = 0
        for j in range(1,n+1):
            if tree_copy[j] and visited[j] == False:
                second_count = bfs(j, visited, tree_copy)
                break
        else:
            second_count = 1
        index += 1
        result = abs(first_count-second_count)
        answer = result if answer > result else answer
        
        
    
    return answer


def bfs(x,visited,tree):
    queue = deque()
    queue.append(x)
    visited[x] = True
    answer = 1
    
    while queue:
        value = queue.popleft()
        for i in tree[value]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                answer += 1
    return answer
    