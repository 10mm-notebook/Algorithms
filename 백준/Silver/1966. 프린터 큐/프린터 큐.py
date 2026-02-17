import sys
from collections import deque 

testcase = int(sys.stdin.readline())

for i in range(testcase):
    N,where=map(int,sys.stdin.readline().split())
    importance = deque(map(int,sys.stdin.readline().split()))
    document = deque(i for i in range(0,N))

    cnt=0
    goal = document[where]
    output=[]

    while True: 
        if importance[0]==max(importance):
            output.append(document.popleft())
            importance.popleft()
                      
            if output[-1]==goal:
                print(len(output))
                break
        else:
            importance.append(importance.popleft())
            document.append(document.popleft())
    
    