# 아침 산책
import sys
from collections import defaultdict
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10 ** 9) #73점에서 멈추는 이유: 아마도 시간초과

cnt = 0 # 경로의 수
N = int(input()) # 노드의 개수
visited = [0 for _ in range(N+1)]
inout = [0] + list(map(int, input().rstrip())) # 실내외 정보 #0:실외 #1:실내
routes = defaultdict(list)
for _ in range(N-1):
    start, end= map(int, input().split(' '))
    routes[start].append(end)
    routes[end].append(start)

def dfs(start):
    tmp = 0
    for next in routes[start]:
        # 인접한 노드가 실내 노드
        if inout[next] == 1:
            tmp += 1
        else: # 인접한 노드가 실외 노드
            if visited[next] != 1:
                visited[next] = 1
                tmp += dfs(next)
    return tmp

def adjIndoor(start):
    tmp = 0
    for next in routes[start]:
        if inout[next] == 1:
            tmp += 1
    return tmp

for start in routes:
    # 본인이 실내야 # 나랑 인접한 실내 1곳 찾아야 해
    if inout[start] == 1:
        cnt += adjIndoor(start)
    else:
        # 본인이 실외야 # 갈 수 있는 실내 2곳 찾아야 해
        ## 인접한 실외를 한 덩어리로 보고 그 덩어리에 인접한 실내의 수를 구한 뒤
        ## 각 덩어리별로 n(n-1)의 경우의 수 계산
        ### n: 인접한 실내 노드의 개수
        #### 헷갈렸던 점: 실외 노드에서 dfs를 타고 가다보면 새로운 실외 노드를 만나게 되는 경우
        #### 실외 노드에 어떤 방식으로든 도착했으면 방문 표시하고 for문에서 해당 노드로 처음 들어가는 경우가 생기면 방문 이력 있음을 알려주면 된다.
        if visited[start] != 1:
            visited[start] = 1
            tmp = dfs(start)
            cnt += tmp * (tmp-1)
print(f'{cnt}')