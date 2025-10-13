import sys
N=int(sys.stdin.readline())



for _ in range(N):
    string=list(sys.stdin.readline().rstrip())
    
    left_string=[]
    status = True

    for i in range(len(string)):
        if string[i]=='(':
            left_string.append(string[i])
        else:
            if left_string:
                left_string.pop()
            else:
                status = False
    if status and len(left_string)==0:
        print('YES')
    else:
        print('NO')