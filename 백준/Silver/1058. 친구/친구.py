import sys

N=int(sys.stdin.readline())

graph=[]

for _ in range(N):
    graph.append(list(sys.stdin.readline().strip()))

max_2_friends = 0

for i in range(N):
    two_friends = set()

    for j in range(N):
        if i == j:
            continue            
        if graph[i][j] == 'Y':
            two_friends.add(j)        
        else:
            for k in range(N):
                if graph[i][k] == 'Y' and graph[k][j] == 'Y':
                    two_friends.add(j)
                    break
    
    if len(two_friends) > max_2_friends:
        max_2_friends = len(two_friends)

print(max_2_friends)