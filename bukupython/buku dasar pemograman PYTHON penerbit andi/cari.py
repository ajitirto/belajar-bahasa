DaftarNama=["Anwar Suadi","Ahmad Jazuli" ,"Safitri","Edi Junaedi","Dian Anggreini","Rahmat anwari"]
dicari=raw_input("penggalan nama yang di cari: ")

indeks=0
ketemu= False

while indeks<=len(DaftarNama):
  if dicari in DaftaraNama[indeks]:
    ketemu=True
    break
  indeks=indeks+1

if ketemu:
  print "nama yang anda cari sama dengan: "
  print DaftarNama[indeks]
else:
  print "tidak ada yang cocok"
