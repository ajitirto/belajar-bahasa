from random import randrange as rand
import Lecture3 as l
import time
import pickle

##K=l.makeA(0,1000000,20000000)
##f=open("store.pckl",'wb')
##pickle.dump(K,f)
##f.close()


f=open("store.pckl",'rb')
K=pickle.load(f)
f.close()

print("get ready")
time.sleep(2)

theRange=100000
step=round((K[-1]-K[0])/theRange)
toFind=range(K[0],K[-1],step)

print("Performing test!")
t=time.time()
for p in toFind:
    j=l.binSeA(K,p)
elapsed=time.time()-t
print(str(elapsed),'seconds')

def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
    
def cariPosisiYangTerkecil(A,dariSini,sampaiSini):
    posisiYangTerkecil=dariSini
    for i in range(dariSini+1,sampaiSini):
        if A[i]<A[posisiYangTerkecil]:
            posisiYangTerkecil=i
    return posisiYangTerkecil

def insertionSort(x):
    for idx,item in enumerate(x):
        print(idx,item)
        
def selectionSort(A):
    n=len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A,i,n)
        if indexKecil != i :
            swap(A,i,indexKecil)
    return A

def cariOMhsYangTerkecil(A,type,dariSini,sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1,sampaiSini):
        if type == "NIM" or type == '1':
            if A[i].NIM < A[posisiYangTerkecil].NIM:
                posisiYangTerkecil = i
        elif type == "uangSaku" or type == '2':
            if A[i].uangSaku < A[posisiYangTerkecil].uangSaku:
                posisiYangTerkecil = i            
        elif type == "kotaTinggal" or type == '3':
            pembanding = [A[posisiYangTerkecil].kotaTinggal,A[i].kotaTinggal];pembanding.sort()
            if pembanding != [A[posisiYangTerkecil].kotaTinggal,A[i].kotaTinggal]:
                posisiYangTerkecil = i    
    return posisiYangTerkecil

def selectionMahasiswaSort(A):
    print ('''
    Welcome to Selection Mahasiswa Sort, Here the selection :
        1. NIM
        2. uangSaku
        3. kotaTinggal
''')
    n=len(A);type=input("Input your selection : ") 
    for i in range(n-1):
        indexKecil = cariOMhsYangTerkecil(A,type,i,n)
        if indexKecil != i :
            swap(A,i,indexKecil)
    return A

def printArray(A):
    for i in A:
        print(i.nama+' '+str(i.NIM)+' '+i.kotaTinggal+' '+str(i.uangSaku))
#mengurutkan nim, kota, uangsaku dari mahasiswa