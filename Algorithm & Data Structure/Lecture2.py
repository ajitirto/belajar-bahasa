class mystr(str):
    def jumlahKata(self):
        return len(self.split())
    
H=[j*j for j in range(8)]
L=[1 for i in range(10)]
Mx=[[z+i for z in range(3)] for i in range(3)]
x=[i**2 for i in range(21) if i%2==0]
S="Yogyakarta Surakarta"
S=[i for i in S if i.lower() in "aiueo"]
T=[(x,x**2) for x in range(6)]

class Node(object):
    "This is Node Class"
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
def kunjungi(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.data)
        currentNode = currentNode.next
##Linked-List
a=Node(11)
b=Node(52)
c=Node(18)
a.next = b
b.next = c

L=[2,52,18,36,13,22,33,44]
a=Node(L[0])

for i in range(len(L)-1):
    s='.next'*(i+1)
    N=Node(L[i+1])
    F='a'+s+' = N'
    exec(F)

def insertFront(n,A):
    a=Node(n)
    a.next = A
    return a

def insertRear(n,A):
    a=Node(n);i=0;Aa=A
    while Aa is not None:
        Aa = Aa.next
        i=i+1
    B = 'A'+'.next'*(i)+'= a'
    exec(B)
    return A