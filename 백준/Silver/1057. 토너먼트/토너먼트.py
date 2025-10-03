N,K_num,L_num = map(int,input().split())
cnt=0

while K_num!=L_num:
    K_num-=K_num//2
    L_num-=L_num//2
    cnt+=1
print(cnt)