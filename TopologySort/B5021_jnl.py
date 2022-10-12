# 왕위 계승
import sys
from collections import defaultdict,deque
input = sys.stdin.readline

N, M= map(int, input().split(' '))
founder = input().rstrip()
inDegree = defaultdict(list)
graph = defaultdict(list)
inDegree[founder] = [0, 0, 1]
for _ in range(N):
    child, father, mother = input().rstrip().split(' ')
    if father not in inDegree:
        inDegree[father] = [0, 0, 0]
    if mother not in inDegree:
        inDegree[mother] = [0, 0, 0]
    if child not in inDegree:
        inDegree[child] = [0, 0, 0]

    # inDegree의 0번 인덱스: 갱신될 인디그리, 1번 인덱스: 오리지널 인디그리, 2번 인덱스: 피  
    # 피는 조상 노드가 끝날때 자식들에게 더해지는 식으로 
    # 조상이 몇명이었는지 기억해야 하므로 오리지널 인디그리를 저장함
    inDegree[child][0] += 2
    inDegree[child][1] += 2
    graph[father].append(child)
    graph[mother].append(child)

nextKing = []
for _ in range(M):
    nextKing.append(input().rstrip())

def solution():
    result = dict()
    queue = deque([])
    for key in inDegree:
        if inDegree[key][0] == 0 and key != founder:
            queue.append([key, 0])
    queue.appendleft([founder, 1])

    while queue:
        me, blood = queue.popleft()
        result[me] = blood
        for child in graph[me]:
            inDegree[child][0] -=1 
            inDegree[child][2] += blood
            if inDegree[child][0] == 0:
                queue.append([child, inDegree[child][2]/inDegree[child][1]])
    
    maxBlood = 0
    answer = ''
    for king in nextKing:
        try:
            if result[king] >  maxBlood:
                maxBlood = result[king]
                answer = king
        except: continue
    return answer

print(solution())
