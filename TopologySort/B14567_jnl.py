# 선수과목
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(' '))
inDegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)] 
for _ in range(M):
    one, two = map(int, input().split(' '))
    inDegree[two]+= 1
    graph[one].append(two)

def solution():
    result = [0 for _ in range(N+1)]
    queue = deque([])
    semester = 1
    for i in range(1, N+1):
        if inDegree[i] == 0:
            queue.append([i, semester])
    while queue:
        nowNode, nowSemester = queue.popleft()
        result[nowNode] = nowSemester
        for nextNode in graph[nowNode]:
            inDegree[nextNode] -= 1
            if inDegree[nextNode] == 0:
                queue.append([nextNode, nowSemester+1])
    
    print(*result[1:])

solution()