import sys

N = int(sys.stdin.readline())
xy_list=[]

for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    xy_list.append([x,y])

def sort(list):
    sorted_xy_list = sorted(list,key=lambda x: (x[0],x[1]))
    for i in range(N):
        print(*sorted_xy_list[i])
    
    return 0

sort(xy_list)