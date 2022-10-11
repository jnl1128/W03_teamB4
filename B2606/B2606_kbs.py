n = int(input())
m = int(input())
graph =[]
visited = [False] * (n+1)
for i in range(n+1):
    graph.append([])
for _ in range(m):
    i,j = map(int, input().split())
    graph[i].append(j)
    if i not in graph[j]:
        graph[j].append(i)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

dfs(1)
count = -1
for i in visited:
    if i:
        count +=1
print(count)