import sys
from collections import deque

def comm(command,i=0):
    if command == 'push':
        queue.append(i)
        
    elif command == 'pop':
        if len(queue)>=1:
            print(queue.popleft())
        else:
            print(-1)
            
    elif command == 'size':
        print(len(queue))
        
    elif command == 'empty':
        if len(queue)>=1:
            print(0)
        else:
            print(1)
            
    elif command == 'front':
        if len(queue)>=1:
            print(queue[0])
        else:
            print(-1)
            
    elif command == 'back':
        if len(queue)>=1:
            print(queue[-1])
        else:
            print(-1)
    return 0


N = int(sys.stdin.readline())
queue=deque()

for i in range(N):
    command_i = sys.stdin.readline().split()
    # command_i=[size,3] 과 같은 형태로 변환
    
    if len(command_i)>=2:
        comm(command_i[0],command_i[1])
    else:
        comm(command_i[0])
    