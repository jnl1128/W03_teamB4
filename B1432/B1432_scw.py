# import sys
# from collections import defaultdict,deque

# input=sys.stdin.readline

# N=int(input())

# A=[]
# for i in range(N):
#     A.append(list(map(int,list(input().strip()))))

# info=defaultdict(set)
# edge=[0]*(N+1)

# for i in range(N):
#     for j in range(N):        
#         if A[i][j]==1:
#             info[i+1].add(j+1)
#             edge[j+1]+=1
#         elif A[i][j]==0 and N==1:
#             info[i+1].add(j+1)

# def solve():
#     result=[]
#     dq=deque()
#     for key in info:
#         if edge[key]==0:
#             dq.append(key)
        
#     while dq:
#         x=dq.popleft()
#         result.append(x)
#         for num in info[x]:
#             edge[num] -=1
#             if edge[num] ==0:
#                 dq.append(num)
    
#     if len(result)!=N:
#         print(-1)
#     else:
#         for i in range(len(result)):
#             for j in range(len(result)):
#                 if i+1 == result[j]:
#                     print(j+1, end=' ')
# solve()


# for i in range(N):
#     for j in range(N):        
#         if A[i][j]==1:
#             info[j+1].add(i+1) # outdgree 간선을 받은 애 (indgree 기준 보낸 애)가 start가 됨
#             edge[i+1]+=1 # outdgree 기준으로 체크 (indgree로 노드가 간선을 보낸 개수를 체크)
#         elif A[i][j]==0 and N==1:
#             info[j+1].add(i+1)


import sys,heapq
from collections import defaultdict

input=sys.stdin.readline

N=int(input().strip())
info=defaultdict(list)
edge=[0]*(N+1) # outdgree
result=[0]*(N+1)
A=[]
for i in range(1,N+1):
    A=(list(map(int,list(input().strip()))))
    for idx, val in enumerate(A):
        if val==1:
            info[idx+1].append(i)
            edge[i]+=1

def solve(N):    
    heap=[]
    for i in range(1, N+1):
        if edge[i]==0: # 간선을 보낸 개수가 0이면 start 노드
            heapq.heappush(heap,(-i, i)) # max heap을 사용하기 위해서 '-'추가
    
    while heap:
        x=heapq.heappop(heap)[1]
        
        result[x]= N
        for num in info[x]:
            edge[num] -=1
            if edge[num] ==0:
                heapq.heappush(heap,(-num,num))
        N-=1

solve(N)

if result.count(0)>2:
    print(-1)
else:
    print(' '.join(map(str, result[1:])))



import sys,heapq
from collections import defaultdict,deque

input=sys.stdin.readline

N=int(input().strip())

A=[]
for i in range(N):
    A.append(list(map(int,list(input().strip()))))

info=defaultdict(set)
edge=[0]*(N+1) # outdgree

for i in range(N):
    for j in range(N):        
        if A[i][j]==1:
            info[j+1].add(i+1) # outdgree 간선을 받은 애 (indgree 기준 보낸 애)가 start가 됨
            edge[i+1]+=1 # outdgree 기준으로 체크 (indgree로 노드가 간선을 보낸 개수를 체크)
        elif A[i][j]==0 and N==1:
            info[j+1].add(i+1)


def solve():
    result=deque()
    heap=[]
    for i in range(1, N+1):
        if edge[i]==0: # 간선을 보낸 개수가 0이면 start 노드
            heapq.heappush(heap,(-i, i)) # max heap을 사용하기 위해서 '-'추가
    while heap:
        x=heapq.heappop(heap)[1]
        result.appendleft(x)
        if x in info:
            for num in info[x]:
                edge[num] -=1
                if edge[num] ==0:
                    heapq.heappush(heap,(-num,num))
    
    if len(result)!=N:
        print(-1)
    else:
        for i in range(len(result)):
            for j in range(len(result)):
                if i+1 == result[j]:
                    print(j+1, end=' ')
solve()