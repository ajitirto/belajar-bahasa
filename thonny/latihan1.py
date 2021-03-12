class MhsTIF(object):
    def __init__(self, nama, thn, kota, us):
        self.nama=nama
        self.thn=thn
        self.kotaTinggal=kota
        self.uangSaku=us
    def __str__(self):
        s=self.nama+" NIM "+str(self.NIM)\
          + " Tinggal Di " + self.kotaTinggal\
          + "  Uang Saku Rp. " + str(self.uangSaku)\
           + "  Tiap Bulannya ="
        return s
    def cetakA(D,s):
        h=[]
        for i in D:
            if i.kotaTinggal ==s:
                h.append(str(i.nama));
        return h
    def cetakB(D):
        b=50000
        for i in D:
            if i.uangSaku <=b:
                b=i.uangsaku
                c=i.nama
            return c
        
    def terkecil(s):
        for i in s:
            if i.usngSaku < s:
                return  (i.nama, i.uangSaku )
        
c0 = MhsTIF('Ika',10,'Sukoharjo', 240000) 
c1 = MhsTIF('Budi',51,'Sragen', 230000) 
c2 = MhsTIF('Ahmad',2,'Surakarta', 250000)
c3 = MhsTIF('Chandra',18,'Surakarta', 235000)
c4 = MhsTIF('Eka',4,'Boyolali', 240000)
c5 = MhsTIF('Fandi',31,'Salatiga', 250000)
c6 = MhsTIF('Deni',13,'Klaten', 245000)
c7 = MhsTIF('Galuh',5,'Wonogiri', 245000)
c8 = MhsTIF('Janto',23,'Klaten', 245000)
c9 = MhsTIF('Hasan',64,'Karanganyar', 270000)
c10 = MhsTIF('Khalid',29,'Purwodadi', 265000)
          
Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

##target ="Surakarta"
##for i in Daftar:
##    if i.kotaTinggal == target:
##        print (i.nama+ ' tinggal di = ' + target)
##  





