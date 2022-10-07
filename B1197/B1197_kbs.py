import sys
v, e = map(int, input().split())
parent = [0]* (v+1)
for i in range(1, v+1):
    parent[i] = i

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

edges = []
total_cost = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for i in range(e):
    cost, a, b = edges[i]
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost
print(total_cost)