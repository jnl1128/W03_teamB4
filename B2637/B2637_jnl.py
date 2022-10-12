# 장난감 조립
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N = int(input()) # 전체 부품 개수 # 노드의 개수
M = int(input()) # 부품들의 관계 개수 # 간선의 개수

# 선수과목(기본 부품) 있는 애들이 차수가 1되는 것임.
# 따라서 중간 이상 부품들의 차수가 1 이상일 될 것
inDegree = [0 for _ in range(N+1)]
graph = [[] for  _ in range(N+1)]
needs = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    x, y, k = map(int, input().split(' '))
    graph[y].append([x, k])
    inDegree[x] += 1

def solution():
    queue = deque([])
    for i in range(1, N+1):
        if inDegree[i] == 0:
            queue.append(i) 
    while queue: 
        q = queue.popleft()
        for n, w in graph[q]:
            # 기본 부품이라면 # needs가 채워지지 않을 것 # 이 부분을 visited로 해야할지에 대해서 헷갈렸음
            if needs[q].count(0) == N+1:
                needs[n][q] += w
            else:
                for i in range(1, N+1):
                    needs[n][i] += needs[q][i] * w
            
            inDegree[n] -= 1
            if inDegree[n] == 0:
                queue.append(n)
    
    for idx, value in enumerate(needs[N]):
        if value != 0:
            print(f'{idx} {value}\n')
    
solution()
