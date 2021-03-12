X=__import__("Practice 4")

A = [1,2,3,4,5,6,7,8,9,10,30,31,32]
B = [2,3,5,10,20,22,28,29,30,33,40]
C = [2,1,4,10,5,4,8,9,3,7,6]

def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A,dariSini,sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1,sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

def bubbleSort(A):
    n=len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
    return A

def selectionSort(A):
    n=len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A,i,n)
        if indexKecil != i :
            swap(A,i,indexKecil)
    return A
    
def insertionSort(A):
    n=len(A)
    for i in range(1,n):
        nilai = A[i]
        pos=i
        while pos>0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos=pos-1
        A[pos] = nilai
    return A
        
def printArray(A):
    for i in A:
        print(i.nama+' '+str(i.NIM)+' '+i.kotaTinggal+' '+str(i.uangSaku))

def cariArrayYangTerkecil(A,dariSini,sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1,sampaiSini):
        if A[i].NIM < A[posisiYangTerkecil].NIM:
            posisiYangTerkecil = i
    return posisiYangTerkecil

def sortArray(A):
    n=len(A)
    for i in range(n-1):
        indexKecil = cariArrayYangTerkecil(A,i,n)
        if indexKecil != i :
            swap(A,i,indexKecil)
    return A
##printArray(X.Daftar)
##x=sortArray(X.Daftar)
##print(" ")
##printArray(x)

def ArrayJoiner(A,B):
    mergedList=A+B
    mergedList=selectionSort(mergedList)
    return mergedList
print(A);print(B)
print(ArrayJoiner(A,B))
from time import time 
from random import shuffle

##k = range(1,6001)
##shuffle(k)
##u_bub=k[:]
##u_sel=k[:]
##u_ins=k[:]
##
##aw=time();bubbleSort(u_bub);ak=time();print("bubble: %g detik"%(ak-aw));
##aw=time();selectionSort(u_sel);ak=time();print("selection: %g detik"%(ak-aw));
##aw=time();insertionSort(u_ins);ak=time();print("insertion: %g detik"%(ak-aw));

from random import randint as rand
def makeA(x,y,z):
    A = [rand(x,y) for i in range(z)]
    return A
##k=makeA(1,6001,6000)
##aw=time();bubbleSort(k);ak=time();print("bubble: %g detik"%(ak-aw));shuffle(k)
##aw=time();selectionSort(k);ak=time();print("selection: %g detik"%(ak-aw));shuffle(k)
##aw=time();insertionSort(k);ak=time();print("insertion: %g detik"%(ak-aw));
