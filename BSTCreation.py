class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insertIntoBST(root,value):
    if root==None:
        newnode=TreeNode(value)
        return newnode

    if root.data>value:
        root.left=insertIntoBST(root.left,value)
    else:
        root.right=insertIntoBST(root.right,value)
    return root
def InOrder(root):
    if root==None:
        return
    InOrder(root.left)
    print(root.data,end=" ")
    InOrder(root.right) 
root=None
nums=[18,10,25,8,15,22,28]
for ele in nums:
    root=insertIntoBST(root,ele)
InOrder(root)

Output
8 10 15 18 22 25 28 
