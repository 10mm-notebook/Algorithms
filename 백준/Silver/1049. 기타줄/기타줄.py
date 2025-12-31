N,M = map(int,input().split())

pack_price=1000
each_price=1000

for i in range(M):
    p,e = map(int,input().split())
    pack_price = min(pack_price,p)
    each_price = min(each_price,e)

how_many_pack = N // 6
remain = N % 6

# 1: 모두 팩으로만 구매할 때
case1 = ((how_many_pack)+1)*pack_price

# 2: 모두 낱개로만 구매할 때
case2 = (each_price)*N

# 3: 우선 팩으로 구매하고 남은 걸 낱개로 구매할 때
case3 = (how_many_pack*pack_price)+(remain*each_price)

    
print(min(case1,case2,case3))