import sys
input = sys.stdin.readline

N,M,k=map(int,input().strip().split())

A={}
for i in range(M):
    city1,city2=map(int,input().strip().split())
    if city1 in A and city2 not in A[city1]:
        A[city1].append(city2)
    elif city1 not in A:
        A[city1]=[city2]
    if city2 in A and city1 not in A[city2]:
        A[city2].append(city1)
    elif city2 not in A:
        A[city2]=[city1]
    
print(A)

visit=[0]*(N+1)

def dfs(v):
    print(v,end='')
    visit[v]=1
    for i in range(1,N+1):
        if visit[i]==0 and i in A[v]:
            dfs(i)

def bfs(v):
    print(v, end='')
    


# for i in A.keys():
#     print(A[i])

dfs(k)
# 순서는 별로 안중요
# 2 -1을 갈 수 있다
'''

1 2 3
2 1 5
3 1 4
4 3 5
5 2 4


'''