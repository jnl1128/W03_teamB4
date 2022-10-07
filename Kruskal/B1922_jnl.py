# 네트워크 연결
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input()) # 컴퓨터 수(노드의 수)
M = int(input()) # 연결선의 수(간선의 수)
parent = [i for i in range(N+1)]
computers = []
for _ in range(M):
    computers.append(list(map(int, input().split(' ')))) # [컴1, 컴2, 가중치]
computers.sort(key=lambda x:x[2])

def findParent(n):
    if n != parent[n]:
        parent[n] = findParent(parent[n])
    return parent[n]

def solution():
    cost = 0 # 전체 비용
    for sComputer, eComputer, weight in computers:
        sParent = findParent(sComputer)
        eParent = findParent(eComputer)

        if sParent != eParent:
            if sParent < eParent:
                parent[eParent] = sParent
            else:
                parent[sParent] = eParent
            cost += weight

    return cost

print(f'{solution()}')

