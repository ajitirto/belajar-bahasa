import re
##string ='sebuah contoh kata:teh!!'
##cocok = re.search(r'kata:\w\w\w', string)
##print (cocok.group())

##cocok = re.search(r'eee','teeeh')#=>ketemu, cocok.group()=="eee"
##cocok = re.search(r'ehs','teeeh')#=>tidak ketemu, cocok==None
##cocok = re.search(r'..h','teeeh')#=>ketemu, cocok.group()=="eeh"
##cocok = re.search(r'\d\d\d','t123h')
##cocok = re.search(r'\w\w\w','@@abcd!!')#=>ketemu, cocok.group()=="abc"

#Pernyataan-IF sesudah search() akan memeriksa apakah pencarian berhasil:
##if cocok:
##    print('menemukan', cocok.group())
##else:
##    print('tidak menemukan')



f=open("Populations.html",'r')
x=re.findall(r'</span><a href="/wiki/[%-_\s\w\,\)\(]+" title="[-_Ã§Ã©\s\w\,\)\(]+">([-_Ã§Ã©\s\w\,\)\(]+)</a>',f.read())
f.close()

class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self)==0
    def isFull(self):
        return len(self)>=512
    def __len__(self):
        return len(self.items)
    def peek(self):
        assert not self.isEmpty(), "Stack Kosong. Tidak bisa di-peek"
        return self.items[-1]
    def pop(self):
        assert not self.isEmpty(), "Stack Kosong. Tidak bisa di-pop"
        return self.items.pop()
    def push(self, data):
        if len(self)==512:
            assert not self.isFull(),"Stack Penuh. Tidak bisa di-push"
        else:
            self.items.append(data)
##x=Stack()
##while True:
##    x.push(1)


def cetakBiner(d):
    f = Stack()
    if d==0: f.push(0);
    while d !=0:
        sisa = d%2
        d = d//2
        f.push(sisa)
    st =""
    for i in range(len(f)):
        st = st +str(f.pop())
    return st
def cetakHexa(d):
    return hex(d)[2:].upper()