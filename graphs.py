#Adjacency matrix
n,m=map(int,input().split())
adj=[]
print(adj)
for i in range(n):
    row=[]
    for j in range(n):
        row.append(0)
    adj.append(row)
for i in range(m):
    u,v=map(int,input().split())
    adj[u][v]=1
    adj[v][u]=1
print(adj)

Input
4 4
1 2
2 2
3 3
1 3

Output
[]
[[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0], [0, 1, 0, 1]]



#Adjacency list 
n, m = map(int, input().split())
adj = []
for i in range(n): 
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
print(adj)

Input
4 4
1 2
2 2
3 3
1 3

Output
[[], [2, 3], [1, 2, 2], [3, 3, 1]]



