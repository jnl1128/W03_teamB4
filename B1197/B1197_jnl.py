# 최소 스패닝 트리
import sys
input = sys.stdin.readline
# print = sys.stdout.write

V, E = map(int, input().split(' '))
result = 0
parent = [i for i in range(V+1)]
routes = list()
for _ in range(E):
    routes.append(list(map(int, input().split(' '))))

routes.sort(key=lambda x:x[2])

# n의 부모를 찾는 과정
def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]


for route in routes:
    [start, end, weight] = route
    sParent = find(start) 
    eParent = find(end)
    if sParent != eParent:
        if sParent > eParent:
            parent[sParent] = eParent
        else:
            parent[eParent] = sParent
        result += weight


print(f'{result}')

