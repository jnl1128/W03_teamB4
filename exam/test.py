from collections import deque


def get_capacity(s,e):
    q = deque()

    q.append(s)

    while True:
        x = q.popleft()
        bc_x= bridge_capacity[x]
        for r in bc_x:

            print(r)
            print(bc_x[r])
            print()


n,m = map(int,input().split())
visited = [False] * (n+1)
bridge_capacity = [None] + [{} for _ in range(n)]
for _ in range(m):
    a,b,cap = map(int,input().split())

    dict_a = bridge_capacity[a]
    if dict_a.get(b)==None:
        dict_a[b]=cap
    else:
        dict_a[b]=max(dict_a[b],cap)

    dict_b = bridge_capacity[b]
    if dict_b.get(a)==None:
        dict_b[a]=cap
    else:
        dict_b[a]=max(dict_b[a],cap)

s,e = map(int,input().split())

get_capacity(s,e)
print()

