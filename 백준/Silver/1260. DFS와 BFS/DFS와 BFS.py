import sys
from collections import deque,defaultdict

N,M,V = map(int,sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()
    

def dfs(graph,start_node):
    visited=[]
    need_visited=deque()

    need_visited.append(start_node)

    while need_visited:
        node=need_visited.pop()

        if node not in visited:
            visited.append(node)
            need_visited.extend(reversed(graph[node]))
            
    return visited

def bfs(graph,start_node):
    visited=[]
    need_visited=deque()

    need_visited.append(start_node)

    while need_visited:
        node=need_visited.popleft()

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
            
    return visited

dfs_result=dfs(graph,V)
bfs_result=bfs(graph,V)

print(" ".join(map(str,dfs_result)))
print(" ".join(map(str,bfs_result)))