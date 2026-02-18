import sys

N=int(sys.stdin.readline())

ropes=[]
max_weight=0

for i in range(N):
    ropes.append(int(sys.stdin.readline()))

ropes.sort(reverse=True)

for k in range(0,N):
    temp = ropes[k]*(k+1)
    max_weight = max(max_weight,temp)

print(max_weight)