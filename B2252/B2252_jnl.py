# 줄세우기
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split(' '))
inDegree = [0 for _ in range(N+1)]
D = [[] for _ in range(N+1)]
answer = []
for _ in range(M):
    one, two = map(int, input().split(' '))
    D[one].append(two)
    inDegree[two] += 1

def solution():
    queue = deque([])
    for i in range(1, N+1):
        if inDegree[i] == 0:
            queue.append(i)

    while queue:
        q = queue.popleft()
        print(f'{q} ')
        for next in D[q]:
            inDegree[next] -= 1
            # inDegree가 0으로 바뀔 부분은 next부분 밖에 없으므로 새로 for문을 만들 필요 없음
            if inDegree[next] == 0:
                queue.append(next)     

solution()