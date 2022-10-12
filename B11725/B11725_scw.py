import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N=int(input())

line_info=defaultdict(list)
while 1:
    try:
        a,b=map(int,input().strip().split())
        line_info[a].append(b)
        line_info[b].append(a)
    except:
        break

visited=[0]*(N+1)

def solve():
    dq=deque()
    dq.append(1)

    while dq:
        x=dq.popleft()
        for i in line_info[x]:
            if visited[i]==0:
                visited[i]=x
                dq.append(i)
solve()

# print(visited)
for i in range(2,len(visited)):
    print(visited[i])