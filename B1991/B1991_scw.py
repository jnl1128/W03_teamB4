import sys

input=sys.stdin.readline

N=int(input())

A={}
for i in range(N):
    root,left,right=input().strip().split()
    A[root]=[left,right]

def preorder(root):
    if root != ".":
        print(root,end="")
        preorder(A[root][0])
        preorder(A[root][1])

def inorder(root):
    if root !=".":
        inorder(A[root][0])
        print(root,end="")        
        inorder(A[root][1])

def postorder(root):
    if root !=".":
        postorder(A[root][0])        
        postorder(A[root][1])
        print(root,end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")