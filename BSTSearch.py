n=int(input())
l=list(map(int,input().split()))
target=int(input())
class TreeNode:
    def _init_(self,data):
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

def SearchInBST(root,target):
    if root==None:
        return False

    elif root.data==target:
        return True
    elif root.data<target:
        return SearchInBST(root.right,target)
   
    return SearchInBST(root.left,target)
root=None
for ele in l:
    root=insertIntoBST(root,ele)
if SearchInBST(root,target):
    print("Target element is found")
else:
    print("Target element is not found")

Sample Input 0
8
8 10 3 18 7 2 81 77
81

Sample Output 0
Target element is found

Sample Input 1
10
80 100 13 28 7 2 81 77 21 22
1001

Sample Output 1
Target element is not found

