#Bottom view
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

def BottomView(root):
    result=[]
    Q=[[root,0]]#First id adress of node and second parameter is horizontal distance of that node
    store=dict()
    while len(Q)>0:
        currPair=Q.pop(0)
        #[address,hd]
        #Q=[[12,0],[3,-1],[5,-2],[10,1]]-->Queue with node address and hd as its fields
        node=currPair[0]
        hd=currPair[1]
        store[hd]=node.data
        if node.left!=None:
            Q.append([node.left,hd-1])
        if node.right!=None:
            Q.append([node.right,hd+1])
    #print(store)
    allkeys=sorted(store.keys())
    for eachkey in allkeys:
        result.append(store[eachkey])
    print("Bottom view of binary tree:",result)

root = TreeNode(18)
obj2 = TreeNode(15)
obj3 = TreeNode(20)
obj4 = TreeNode(25)
obj5 = TreeNode(30)
obj6 = TreeNode(45)
obj7 = TreeNode(80)
root.left = obj2 
root.right = obj3  
obj2.left = obj4 
obj2.right = obj5 
obj3.left = obj6 
obj3.right = obj7
BottomView(root)

Output
Bottom view of binary tree: [25, 15, 45, 20, 80]

