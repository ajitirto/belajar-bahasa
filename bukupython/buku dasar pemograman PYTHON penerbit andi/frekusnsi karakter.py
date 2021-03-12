
jumkar={}
kalimat=raw_input("masukan suatu kalimat :")
for kar in kalimat:
  jumkar[kar] = jumkar.get(kar,0) +1
  
#menampilkan frekueb=nsi karakter:
for kar in jumkar.keys():
  if kar == " ":
    print "spasi"
  else:
    print kar, "="
  print jumkar[kar]
  


    
