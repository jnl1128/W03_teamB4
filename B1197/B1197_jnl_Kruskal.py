# 최소 스패닝 트리 # Kruskal
# best case: O(E + VlogE) == O(E+VlogV) => O(ElogE)
import sys, heapq
input = sys.stdin.readline
print = sys.stdout.write

V, E = map(int, input().split(' '))
result = 0
parent = [i for i in range(V+1)]
routes = []
for _ in range(E):
    start, end, weight = map(int, input().split(' '))
    heapq.heappush(routes, [weight, start, end])
# heap을 안쓰려면 가중치 기준 오름차순으로 sort해야 함 

# n의 부모를 찾는 과정
def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]

while routes:
    [weight,start, end] = heapq.heappop(routes)
    sParent = find(start) 
    eParent = find(end)
    if sParent != eParent:
        if sParent > eParent:
            parent[sParent] = eParent
        else:
            parent[eParent] = sParent
        result += weight


print(f'{result}')

