##str=raw_input("masukan nilai: ")
##print ("\ntampilkan string yang di masukan sebanyak 10*\n")
##i=1
##while (i<=100):
##  print i,".",str
##  i+=1
##  
##  
##pilih = "y"
##while(pilih):
##    nama=raw_input("masukan nama: ")
##    tahunlahir=raw_input("tahun lahir: ")
##    tahunsekarang=raw_input("tahunsekarang: ")
##    umur = tahunsekarang - tahunlahir
##    print nama,"umur anda adlah: ",umur,"tahun"

##print("membangkitkan nilai dengan rentang waktu tertentu")
##print("-------------------------------------------------")
##awal = int(raw_input("masukan batasan awal: "))
##akhir= int(raw_input("masukan batasan akhir: "))
##print("\nnilai yang anda inginkan adalah\n")
##for i in range(awal,akhir):
##  print i

##jum=int(raw_input("masukan jumlah element list: "))
##print("\nsilahkan masukan element list\n")
##print("----------------------------------")
##list=[]
##for i in range(jum):
##  i=1
##  element=raw_input((i+1),":")
##  list.insert(i,element)
##print("\nisi list adalah\n")
##print("--------------------")
##for j in range(jum):
##  print list(j)
##        

##data=[10,29,4,6,4,3,1,2,12,23,6767,45,343,13,324,6,54,435,435,25,343645654,7,6767,6,4674,54,564,564645,65,56
##      ,345345,6564,546]
##print("isi dari list")
##print("-------------")
##for i in data:
##  print i
##print("\nisilist yang sudah i urutkan\n")
##print("---------------------------------")
##for j in sorted(data):
##  print j

import turtle
t = turtle
t.pen()
for i in range(205,300,10):
  t.fd(i)
  t.left(360)
  
