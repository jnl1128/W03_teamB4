import sys
input = sys.stdin.readline

N,M,k=map(int,input().strip().split())

A={}
for i in range(M):
    city1,city2=map(int,input().strip().split())
    if city1 in A:
        A[city1].append(city2)
    else:
        A[city1]=[city2]

