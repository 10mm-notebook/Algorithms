import sys

def push(X):
    stack.append(X)

def pop():
    if not stack:
        return -1
    else:
        return stack.pop()
        
def size():
    return (len(stack))
    
def empty():
    if len(stack)>0:
        return 0
    else:
        return 1
        
def top():
    if not stack:
        return -1
    else:
        return stack[-1]
    

N=int(sys.stdin.readline())
stack=[]

for _ in range(N):
    command = sys.stdin.readline().strip()
    
    if 'push' in command:
        command_push,num=command.split()
        push(num)        
    elif command=='top':
        print(top())
    elif command=='pop':
        print(pop())
    elif command=='size':
        print(size())
    elif command=='empty':
        print(empty())
