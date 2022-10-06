# 트리 순회
import sys 
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
D = dict()
for _ in range(N):
    parent, left, right = input().rstrip().split(' ')
    D[parent] = [left, right]

def preOrder(parent):
    print(parent)
    [left, right] = D[parent]
    if left == '.' and right == '.':
        return
    for child in D[parent]:
        if child != '.':
            preOrder(child)
    return


def inOrder(parent):
    [left, right] = D[parent]
    if left != '.':
        inOrder(left)
    print(parent)
    if right != '.':
        inOrder(right)


def postOrder(parent):
    [left, right] = D[parent]
    if left != '.':
        postOrder(left)
    if right != '.':
        postOrder(right)
    print(parent)


def solution():
    preOrder('A')
    print('\n')
    inOrder('A')
    print('\n')
    postOrder('A')

solution()
