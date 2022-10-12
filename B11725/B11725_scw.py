import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N=int(input())

line_info=defaultdict(list)
while 1:
    try:
        a,b=map(int,input().strip().split()) # 양방향 탐색을해서 트리부터 찾아가야하기때문에 양쪽으로 저장
        line_info[a].append(b)
        line_info[b].append(a)
    except:
        break

visited=[0]*(N+1)

def solve():
    dq=deque()
    dq.append(1) # 첫 시작점이 1이기 때문에 1을 넣어줌

    while dq:
        x=dq.popleft()
        for i in line_info[x]:
            if visited[i]==0:
                visited[i]=x
                dq.append(i)
solve()

# print(visited)
for i in range(2,len(visited)): # 1은 부모가 없기때문에 제외하고 출력
    print(visited[i])