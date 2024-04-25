#Boundary Traversal
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

def collectLeftBoundary(root,result):
    while root!=None:
        if root.left==None and root.right==None:
             break
        result.append(root.data)
        if root.left!=None:
            root=root.left
        else:
            root=root.right
def collectLeafNodes(root,result):
    if root==None:
        return
    if root.left==None and root.right==None:
        result.append(root.data)
        return
    collectLeafNodes(root.left,result)
    collectLeafNodes(root.right,result)
def collectRightBoundary(root,result):
    temp = []
    while root != None:
        if root.left == None and root.right == None:
            break
        temp.append(root.data)
        if root.right != None:
            root = root.right 
        else:
            root = root.left
    temp = temp[::-1]
    for ele in temp:
        result.append(ele)
    
def BoundaryTraversal(root):
    result=[]
    result.append(root.data)
    #1.Collect left boundary
    collectLeftBoundary(root.left,result)
    #2.Collect leaf node(in left to right direction)
    collectLeafNodes(root,result)
    #3.Collect right boundary(in reverse direction)
    collectRightBoundary(root.right,result)
    print("Boundary traversal is:",result)
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
BoundaryTraversal(root)

Output
Boundary traversal is: [18, 15, 25, 30, 45, 80, 20]
