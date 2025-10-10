import sys
from collections import deque,defaultdict

def dfs(graph,start_node):
    visited=[]
    need_visited=deque()

    need_visited.append(start_node)

    while need_visited:
        node=need_visited.pop()

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])

    return visited
        
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

graph= defaultdict(list)

for _ in range(M):
    n1,n2=map(int,sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

print(len(dfs(graph,1))-1)
