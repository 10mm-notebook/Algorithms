import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
B,C=map(int,sys.stdin.readline().split())

director=N

for _ in range(N):
    A[_]-=B
    if A[_]>0:
        
        director+=A[_]//C
        remain=A[_]%C

        if remain!=0:
            director+=1
        

print(director)