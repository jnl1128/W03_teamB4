import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)

input=sys.stdin.readline


def check_list(a) : #DFS
    for i in line[a]:
        k=i        
        if visited[k]==1 and i==line[a][len(line[a])-1]:            
            return
        elif visited[k]==0:
            visited[k]=1
            check_list(k)
    return

N, M=map(int,input().strip().split())

line=defaultdict(list)
for i in range(M): # 방향이 없기 때문에 양방향으로 dictionary를 만들음
    a, b=map(int,input().strip().split())
    line[a].append(b)
    line[b].append(a)

for i in line: # 딕셔너리 내부의 value를 정렬함
    line[i].sort()
cnt=0
visited=[0]*(N+1)

for key in range(1, N+1):
# for key in line.keys():
    a=key
    if visited[a]==0:
        visited[a]=1
        cnt+=1
        check_list(a)
    else:
        check_list(a)
        
if N==1:
    print(1)
else:
    print(cnt)

