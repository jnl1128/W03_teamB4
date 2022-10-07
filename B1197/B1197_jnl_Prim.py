# 최소 스패닝 트리 # Prim
# Prim은 간선의 개수가 적을 때 Kruskal보다 강력함
import sys, heapq
input = sys.stdin.readline 
print = sys.stdout.write

V, E = map(int, input().split(' ')) # V: 노드의 개수, E: 간선의 개수
nodes = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
for _ in range(E):
    start, end, weight = map(int, input().split(' '))
    nodes[start].append([weight, end])
    nodes[end].append([weight, start])

cost = 0
heap = [[0, 1]]
# sum(visited) == V로 끝나는거 체크하거나 all(visited[1:])로 하면 시간초과됨
    # 두 방법으로 하면 visited라는 배열의 모든 원소를 조회해야 하니까 시간초과 나는 듯
# cnt를 하나씩 올려주면서 cnt == V가 되면 끝나는거 체크하면 통과함
cnt = 0
while heap:
    if cnt == V:
        break
    [weight, node] = heapq.heappop(heap)
    if visited[node] != 1:
        visited[node] = 1
        cost += weight
        cnt += 1
        for nextNode in nodes[node]:
            heapq.heappush(heap, nextNode)
    
print(f'{cost}')