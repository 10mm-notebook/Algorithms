import sys

N=int(sys.stdin.readline())
cnt=0

for i in range(N):
    word=list(sys.stdin.readline())
    checker=[]
    
    status=True

    for j in range(len(word)):
        checker.append(word[j])

        if (word[j] not in checker[0:j-1]) or (checker[j-1]==word[j]):
            pass
        else:
            status=False


    if status:
        cnt+=1

print(cnt)