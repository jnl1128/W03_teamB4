import sys
from collections import deque
input = sys.stdin.readline
# print = sys.stdout.write

leftSubTree = deque([])
rightSubTree = deque([])
arr = deque([])
while True:
    try:
        node = int(input())
    except:
        break
    arr.append(node)
root = arr[0]
while arr:
    a = arr.popleft()
    if a < root:
        leftSubTree.append(a)
    else:
        rightSubTree.append(a)
    
result = []
def solution():
    left = []
    right = []
    
    while leftSubTree:
        l = leftSubTree.popleft()
        if len(left) == 0:
            left.append(l)
            continue
        if left[-1] > l:
            left.append(l)

        

        
