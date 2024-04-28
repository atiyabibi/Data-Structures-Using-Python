def DFSTraversal(adj,n):
    visited=[False]*n
    result=[]
    for i in range(n):
        if visited[i]==False:
            initiateDFS(i,visited,adj,result)
    print(result,end=" ")

def initiateDFS(node,visited,adj,result):
    result.append(node)
    visited[node]=True
    for n in adj[node]:
        if visited[n]==False:
            initiateDFS(n,visited,adj,result)

n, m = map(int, input().split())
adj = []
for i in range(n): 
    adj.append([])
for i in range(m):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
DFSTraversal(adj,n)


Input
11 10
0 1 
0 2
0 3
1 4
4 6 
4 5
7 8
7 9
9 10
8 10

Output
[0, 1, 4, 6, 5, 2, 3, 7, 8, 10, 9] 
