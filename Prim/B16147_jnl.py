# 도시 분할 계획
# 간선의 개수가 1,000,000 이하이고, 노드의 개수가 100,000 이하이다.
# 1st Trial: 간선의 수가 많으므로 노드 중심의 Prim 알고리즘을 사용할 것 -> 시간초과
    # Kruskal: O(ElogE) -> 1000000 * 6  = 6,000,000
    # Prim: O(V^2) -> 100000 * 100000 = 10,000,000,000
        # => 1st Trial는 완전 잘못된 생각... 
# 2nd Trial: 그렇다면 Kruskal 알고리즘 -> 통과(2262264kb 6744ms)

import sys, heapq
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split(' '))
parent = [i for i in range(N+1)]
routes = []
for _ in range(M):
    start, end, weight = map(int, input().split(' '))
    heapq.heappush(routes, [weight, start, end])

def findParent(n):
    if n != parent[n]:
        parent[n] = findParent(parent[n])
    return parent[n]

def solution():
    totalWeight = 0
    maxWeight = 0
    while routes:
        w, s, e = heapq.heappop(routes)
        sParent = findParent(s)
        eParent = findParent(e)
        if sParent != eParent:
            if sParent < eParent:
                parent[eParent] = sParent
            else:
                parent[sParent] = eParent
            totalWeight += w
            maxWeight = max(maxWeight, w)

    print(f'{totalWeight-maxWeight}')
solution()