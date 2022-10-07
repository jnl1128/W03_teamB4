import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)

input=sys.stdin.readline

N=int(input().strip())
L=int(input().strip())
com=defaultdict(list)
for i in range(L):
    a,b=map(int, input().strip().split())
    com[a].append(b)
    com[b].append(a)

virus_list=[0]*(N+1)
for i in com:
    com[i].sort()

def virus(v):    
    for i in com[v]:        
        if virus_list[i] ==1 and i==com[v][len(com[v])-1]:
            return
        elif virus_list[i]==0:
            virus_list[i]=1
            virus(i)

virus(1)
if sum(virus_list)-1<=0:
    print(0)
else:
    print(sum(virus_list)-1)