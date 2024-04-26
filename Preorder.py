#Preorder traversal
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

def PreOrder(root):
    if root==None:
        return
    print(root.data,end=" ")
    PreOrder(root.left)
    PreOrder(root.right)

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
PreOrder(root)

Output
18 15 25 30 20 45 80 

