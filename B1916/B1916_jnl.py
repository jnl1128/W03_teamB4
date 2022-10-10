# 최소비용 구하기
import sys, heapq
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
M = int(input())
visited = [sys.maxsize]*(N+1) # 초기값이 maxsize이고, 갈 수 있는 경로가 있음에도 maxsize라는 것은 아직 방문하지 않았다는 의미이다.
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, weight = map(int, input().split(' '))
    graph[start].append([weight, end])
startNode, endNode = map(int, input().split(' '))

def dijkstra(start):
    pq = []
    heapq.heappush(pq, [0, start])
    visited[start] = 0

    while pq:
        d, x = heapq.heappop(pq)
        
        # d는 0이상인 수이다. # visited[x]가 d보다 작다는 것은 이미 최솟값이라는 의미이다.
        if visited[x] < d: 
            continue
        
        for nw, nx in graph[x]:
            # d: start에서 x까지 오는데 쓴 비용
            # nw: x에서 nx로 가는데 쓸 비용
            nd = nw + d
        
            # 현재 루트가 start에서 nx으로 가는데 최소 비용이라면
            if nd < visited[nx]:
                heapq.heappush(pq, (nd, nx))
                visited[nx] = nd

dijkstra(startNode)
print(f'{visited[endNode]}')
 