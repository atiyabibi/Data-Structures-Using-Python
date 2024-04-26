#PostOrder traversal
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

def PostOrder(root):
    if root==None:
        return
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.data,end=" ")

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
PostOrder(root)

Output
25 30 15 45 80 20 18 
