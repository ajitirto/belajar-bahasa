class _BinaryTreeNode(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
A = _BinaryTreeNode('Ambarawa')
B = _BinaryTreeNode('Bantul')
C = _BinaryTreeNode('Cimahi')
D = _BinaryTreeNode('Denpasar')
E = _BinaryTreeNode('Enrekang')
F = _BinaryTreeNode('Flores')
G = _BinaryTreeNode('Garut')
H = _BinaryTreeNode('Halmahera Timur')
I = _BinaryTreeNode('Indramayu')
J = _BinaryTreeNode('Jakarta')

A.left=B;A.right=C
B.left=D;B.right=E
C.left=F;C.right=G
E.left=H;G.right=I

def preorderTrav(subtree):
    if subtree is not None:
        print(subtree.data)
        preorderTrav(subtree.left)
        preorderTrav(subtree.right)
def inorderTrav(subtree):
    if subtree is not None:
        inorderTrav(subtree.left)
        print(subtree.data)
        inorderTrav(subtree.right)
def postorderTrav(subtree):
    if subtree is not None:
        postorderTrav(subtree.left)
        postorderTrav(subtree.right)
        print(subtree.data)
        
def widthTree(root):
    h=heightTree(root)
    arr=[0]*h
    getwidthTree(root,arr,0)
    return max(arr)
def getwidthTree(root,arr,level):
    if root is not None:
        arr[level]+=1
        getwidthTree(root.left,arr,level+1)
        getwidthTree(root.right,arr,level+1)
        
def heightTree(root):
    if root is None:
        return 0
    else:
        left=heightTree(root.left)
        right=heightTree(root.right)
        return (left+1) if(left>right) else(right+1)
        
def printDataandLevel(root):
    reprintDataandLevel(root,0)
def reprintDataandLevel(root,level):
    if root is not None:
        print(root.data+", Level = "+str(level))
        reprintDataandLevel(root.left,level+1)
        reprintDataandLevel(root.right,level+1)        
        