import sys
read = sys.stdin.readline

n = int(read())
m = int(read())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
edges = []
total_cost = 0

for _ in range(m):
    a, b, cost = map(int, read().rstrip().split())
    edges.append((cost, a, b))
edges.sort()

for i in range(m):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost
print(total_cost)