def BFSTraversal(adj,n):
    visited=[False]*n
    result=[]
    for i in range(n):
        if visited[i]==False:
            storeBFS(i,result,adj,n,visited)
    print("BFS is:",result)

def storeBFS(startNode,result,adj,n,visited):
    visited[startNode]=True
    Q=[startNode]
    while len(Q)>0:
        currNode=Q.pop(0)
        result.append(currNode)
        for n in adj[currNode]:#n=neighbour
            if visited[n]==False:
                visited[n]=True
                Q.append(n)

n, m = map(int, input().split())
adj = []
for i in range(n): 
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

BFSTraversal(adj,n)

Input
6 9
1 2
3 4
5 5
2 1
4 3
1 5
2 4
3 3
1 1

Output
BFS is: [0, 1, 2, 5, 4, 3]
