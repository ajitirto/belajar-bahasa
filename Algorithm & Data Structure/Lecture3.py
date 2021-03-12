class MhsTIF(object):
    """Class mahasiswa dengan berbagai metode"""
    def __init__(self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s =self.nama +', NIM '+str(self.NIM) \
        +'.Tinggal di '+self.kotaTinggal \
        +'.Uangsaku Rp '+str(self.uangSaku) \
        +' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku

c0=MhsTIF('Ika',10,'Sukoharjo',240000)
c1=MhsTIF('Budi',51,'Sragen',230000)
c2=MhsTIF('Ahmad',2,'Surakarta',250000)
c3=MhsTIF('Chandra',10,'Surakarta',235000)
c4=MhsTIF('Eka',4,'Boyolali',240000)
c5=MhsTIF('Fandi',31,'Salatiga',250000)
c6=MhsTIF('Debi',13,'Klaten',245000)
c7=MhsTIF('Galuh',5,'Wonogiri',245000)
c8=MhsTIF('Janto',23,'Klaten',245000)
c9=MhsTIF('Hasan',64,'Karanganyar',270000)
c10=MhsTIF('Khalid',29,'Purwodadi',265000)

Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
def cariKota(D,s):
    result=[]
    for i in D:
        if i.kotaTinggal == s:
            result.append(i)
    return result
def cariUangSaku(D,s):
    result=[]
    for i in D:
        a='i.uangSaku'+s
        if eval(a):
            result.append(i.nama)
    return result
def cariTerkecil(D):
    terkecil = D[0].uangSaku;x=0
    for i in range(len(D)):
        if D[i].uangSaku<terkecil:
            terkecil=D[i].uangSaku
            x=i
    return (D[x].nama,D[x].uangSaku)
def cariTerbesar(D):
    terbesar = D[0].uangSaku;x=0
    for i in range(len(D)):
        if D[i].uangSaku>terbesar:
            terbesar=D[i].uangSaku
            x=i
    return (D[x].nama,D[x].uangSaku)
def cariKotaA(D):
    x="abcdefghijklmnopqrstuvwxyz";x1=0
    for i in x.upper():
        if x1!=0:
            break
        for j in range(len(D)):
            if i == D[j].kotaTinggal[0]:
                x1=j
                break
    return (D[x1].nama,D[x1].kotaTinggal)
def cariKotaB(D):
    x="abcdefghijklmnopqrstuvwxyz";x1=0
    for i in x.upper():
        for j in range(len(D)):
            if i == D[j].kotaTinggal[0]:
                x1=j
    return (D[x1].nama,D[x1].kotaTinggal)



G=[1,1,1,5,6,6,8,10,11,11,13,13,14,14,17,20,20,21,22,24]
F=[1,5,6,6,8,10,11,11,13,13,14,14,17,20,20,21,22,24]
from random import randrange as rand
def makeA(x,y,z):
    A = [rand(x,y) for i in range(z)];A.sort()
    return A
def binSeA(list,target):
    low=0;high=len(list)-1;x=1;y=1
    while low<=high:
        mid=(high+low)//2
        if list[mid]==target:
            while mid+y<=len(list)-1 and list[mid+y]==target:
                y=y+1
            while mid-x>=0 and list[mid-x]==target:
                x=x+1
            if x==1 and y==1:
                return(mid,)
            else:
                return(mid-(x-1),mid+(y-1))
        elif target < list[mid]:
            high=mid-1
        else:
            low=mid+1
    return False

