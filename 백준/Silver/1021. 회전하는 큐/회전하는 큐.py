import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
M_nums = list(map(int, sys.stdin.readline().split())) 
queue = deque(range(1, N + 1))

count = 0
for num in M_nums:
    idx = queue.index(num)

    if idx < len(queue) - idx:
        count += idx
        queue.rotate(-idx) 
    else:
        count += len(queue) - idx
        queue.rotate(len(queue) - idx) 
        
    queue.popleft()

print(count)