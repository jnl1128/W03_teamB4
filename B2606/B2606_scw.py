import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N=int(input().strip())
L=int(input().strip())
com=defaultdict(list)
for i in range(L): # 바이러스는 연결만 되어있으면 이동이 가능하니 양방향으로 탐색을 해야함
    a,b=map(int, input().strip().split())
    com[a].append(b)
    com[b].append(a)

virus_list=[0]*(N+1)
for i in com: # 딕셔너리 value를 정렬
    com[i].sort()

def virus(v): #DFS
    for i in com[v]:        
        if virus_list[i] ==1 and i==com[v][len(com[v])-1]:
            return
        elif virus_list[i]==0:
            virus_list[i]=1
            virus(i)

virus(1)
if sum(virus_list)-1<=0: # 자기 자신은 빼야함
    print(0)
else:
    print(sum(virus_list)-1) # 자기자신을 빼야함