#Kth largest and smallest
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

def fillInOrder(inorder,root):
    if root==None:
        return
    fillInOrder(inorder,root.left)
    inorder.append(root.data)
    fillInOrder(inorder,root.right) 

root=None
nums=[18,10,25,8,15,22,28]
for ele in nums:
    root=insertIntoBST(root,ele)

#Kth smallest element
k=3
inorder=[]
fillInOrder(inorder,root)
print(inorder[k-1])

#Kth largest element
k=3
inorder=[]
fillInOrder(inorder,root)
inorder=inorder[::-1]
print(inorder[k-1])

Output
15
22
