#ZigZag level order
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
def printZigZagLevelOrder(root):
    result = []
    Q = [root]
    level = 0 
 
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            curr = Q.pop(0)
            subResult.append(curr.data)
            if curr.left != None:
                Q.append(curr.left)
            if curr.right != None:
                Q.append(curr.right)
        if level % 2 == 1:
            subResult = subResult[::-1]#Prints the list in reverse order
        result.append(subResult)
        level += 1 
    for subLevel in result:
        print(*subLevel) 

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
printZigZagLevelOrder(root)

Output
18
20 15
25 30 45 80
