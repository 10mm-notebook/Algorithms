import sys

N=int(sys.stdin.readline())

appro_5=N//5
the_min_bag=5000
status=False

for i in range(appro_5,-1,-1):
    M=N
    M-=(5*i)
    min_bag=i

    if M==0:
        status=True
        the_min_bag=min(the_min_bag,min_bag)
        
    else:
        min_bag+=(M//3)
        M-=(3*(M//3))
        if M==0:
            status = True
            the_min_bag=min(the_min_bag,min_bag)

if status and the_min_bag!=5000:
    print(the_min_bag)
else:
    print(-1)
    