class Queue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self.qlist)
    
    def enqueue( self, data ):
        self.qlist.append(data)
    def dequeue(self):
        if self.isEmpty():
            return "Antrian sedang kosong."
        return self.qlist.pop(0)
    
        
    
class GDPCountry(object):
    def __init__(self, nama, data, priority):
        self.name = nama
        self.data = data
        self.prty = priority
    def __str__(self):
        print (self.name+", US$"+str(self.data))

A=GDPCountry("Jerman",46.251,1)
B=GDPCountry("Uni Emirat Arab",43.048,2)
C=GDPCountry("Irlandia",50.478,3)
D=GDPCountry("Finlandia",49.150,4)
E=GDPCountry("Islandia",47.349,5)
F=GDPCountry("Belgia",46.929,6)
G=GDPCountry("Belanda",50.792,7)
H=GDPCountry("Austria",50.510,8)
I=GDPCountry("Kuwait",52.197,9)
J=GDPCountry("Amerika Serikat",53.041,10)
K=GDPCountry("Luksemburg",110.664,11)
L=GDPCountry("Norwegia",112.832,12)
M=GDPCountry("Macao SAR, China",91.376,13)
N=GDPCountry("Swiss",84.748,14)
O=GDPCountry("Qatar",93.714,15)
P=GDPCountry("Australia",67.463,16)
Q=GDPCountry("Swedia",60.380,17)
R=GDPCountry("Singapura",55.182,18)
S=GDPCountry("Denmark",59.818,19)
T=GDPCountry("Belanda",50.792,20)

Lists=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T]

k=Queue()

k.enqueue(A)
k.enqueue(B)
k.enqueue(C)
k.enqueue(D)
k.enqueue(E)
k.enqueue(F)
k.enqueue(G)
k.enqueue(H)
k.enqueue(I)
k.enqueue(J)
k.enqueue(K)
k.enqueue(L)
k.enqueue(M)
k.enqueue(N)
k.enqueue(O)
k.enqueue(P)
k.enqueue(Q)
k.enqueue(R)

k.dequeue().name




