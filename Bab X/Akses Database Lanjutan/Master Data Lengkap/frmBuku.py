#Boa:Frame:Frame1

import wx, MySQLdb,os
import datetime 
conn= MySQLdb.connect(host="localhost", user="root", passwd="",db="perpus")
cur = conn.cursor()


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1CMBKATEGORI, wxID_FRAME1GAMBAR, wxID_FRAME1LC, 
 wxID_FRAME1PANEL1, wxID_FRAME1RTIDAK, wxID_FRAME1RYA, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, 
 wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, wxID_FRAME1TGL_MASUK, 
 wxID_FRAME1TMBBERSIH, wxID_FRAME1TMBBROWSE, wxID_FRAME1TMBHAPUS, 
 wxID_FRAME1TMBSIMPAN, wxID_FRAME1TXT_JUDUL, wxID_FRAME1TXT_KDBUKU, 
 wxID_FRAME1TXT_PATH, wxID_FRAME1TXT_STOCK, wxID_FRAME1TXT_TINGGI, 
] = [wx.NewId() for _init_ctrls in range(26)]

class Frame1(wx.Frame):
    def _init_coll_lc_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Kode Buku', width=90)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Judul',
              width=165)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='Stock',
              width=-1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(370, 120), size=wx.Size(478, 558),
              style=wx.DEFAULT_FRAME_STYLE, title='Data Buku')
        self.SetClientSize(wx.Size(462, 520))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(462, 520),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Kode Buku', name='staticText1', parent=self.panel1,
              pos=wx.Point(16, 10), size=wx.Size(50, 13), style=0)

        self.txt_kdbuku = wx.TextCtrl(id=wxID_FRAME1TXT_KDBUKU,
              name='txt_kdbuku', parent=self.panel1, pos=wx.Point(104, 10),
              size=wx.Size(100, 21), style=wx.TE_PROCESS_ENTER, value='')
        self.txt_kdbuku.Bind(wx.EVT_TEXT_ENTER, self.OnTxt_kdbukuTextEnter,
              id=wxID_FRAME1TXT_KDBUKU)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Judul', name='staticText2', parent=self.panel1,
              pos=wx.Point(16, 49), size=wx.Size(25, 13), style=0)

        self.txt_judul = wx.TextCtrl(id=wxID_FRAME1TXT_JUDUL, name='txt_judul',
              parent=self.panel1, pos=wx.Point(104, 41), size=wx.Size(168, 21),
              style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Kategori', name='staticText3', parent=self.panel1,
              pos=wx.Point(16, 97), size=wx.Size(40, 13), style=0)

        self.cmbkategori = wx.ComboBox(choices=[], id=wxID_FRAME1CMBKATEGORI,
              name='cmbkategori', parent=self.panel1, pos=wx.Point(103, 97),
              size=wx.Size(130, 21), style=0, value='')
        self.cmbkategori.SetLabel('')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label='Dipinjam', name='staticText4', parent=self.panel1,
              pos=wx.Point(16, 145), size=wx.Size(40, 13), style=0)

        self.rYa = wx.RadioButton(id=wxID_FRAME1RYA, label='Ya', name='rYa',
              parent=self.panel1, pos=wx.Point(102, 145), size=wx.Size(81, 13),
              style=0)
        self.rYa.SetValue(False)

        self.rTidak = wx.RadioButton(id=wxID_FRAME1RTIDAK, label='Tidak',
              name='rTidak', parent=self.panel1, pos=wx.Point(232, 145),
              size=wx.Size(81, 13), style=0)
        self.rTidak.SetValue(False)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label='staticText5', name='staticText5', parent=self.panel1,
              pos=wx.Point(-80, 8), size=wx.Size(54, 13), style=0)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label='Tanggal Masuk', name='staticText6', parent=self.panel1,
              pos=wx.Point(16, 193), size=wx.Size(71, 13), style=0)

        self.tgl_masuk = wx.DatePickerCtrl(id=wxID_FRAME1TGL_MASUK,
              name='tgl_masuk', parent=self.panel1, pos=wx.Point(104, 193),
              size=wx.Size(90, 21), style=wx.DP_SHOWCENTURY)
        self.tgl_masuk.SetValue(wx.DateTimeFromDMY(17, 1, 2011, 0, 0, 0))
        self.tgl_masuk.SetLabel('17/2/2011')

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label='Stock', name='staticText7', parent=self.panel1,
              pos=wx.Point(16, 241), size=wx.Size(26, 13), style=0)

        self.txt_stock = wx.TextCtrl(id=wxID_FRAME1TXT_STOCK, name='txt_stock',
              parent=self.panel1, pos=wx.Point(104, 233), size=wx.Size(100, 21),
              style=0, value='')

        self.tmbSimpan = wx.Button(id=wxID_FRAME1TMBSIMPAN, label='Simpan',
              name='tmbSimpan', parent=self.panel1, pos=wx.Point(16, 320),
              size=wx.Size(75, 23), style=0)
        self.tmbSimpan.Bind(wx.EVT_BUTTON, self.OnTmbSimpanButton,
              id=wxID_FRAME1TMBSIMPAN)

        self.tmbHapus = wx.Button(id=wxID_FRAME1TMBHAPUS, label='Hapus',
              name='tmbHapus', parent=self.panel1, pos=wx.Point(112, 320),
              size=wx.Size(75, 23), style=0)
        self.tmbHapus.Bind(wx.EVT_BUTTON, self.OnTmbHapusButton,
              id=wxID_FRAME1TMBHAPUS)

        self.tmbBersih = wx.Button(id=wxID_FRAME1TMBBERSIH, label='Bersih',
              name='tmbBersih', parent=self.panel1, pos=wx.Point(200, 320),
              size=wx.Size(75, 23), style=0)
        self.tmbBersih.Bind(wx.EVT_BUTTON, self.OnTmbBersihButton,
              id=wxID_FRAME1TMBBERSIH)

        self.lc = wx.ListCtrl(id=wxID_FRAME1LC, name='lc', parent=self.panel1,
              pos=wx.Point(16, 355), size=wx.Size(416, 152),
              style=wx.LC_REPORT)
        self._init_coll_lc_Columns(self.lc)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnLcListItemSelected,
              id=wxID_FRAME1LC)

        self.gambar = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GAMBAR, name='gambar', parent=self.panel1,
              pos=wx.Point(344, 40), size=wx.Size(80, 136), style=0)

        self.tmbBrowse = wx.Button(id=wxID_FRAME1TMBBROWSE, label='Browse',
              name='tmbBrowse', parent=self.panel1, pos=wx.Point(344, 192),
              size=wx.Size(75, 23), style=0)
        self.tmbBrowse.Bind(wx.EVT_BUTTON, self.OnTmbBrowseButton,
              id=wxID_FRAME1TMBBROWSE)

        self.txt_path = wx.TextCtrl(id=wxID_FRAME1TXT_PATH, name='txt_path',
              parent=self.panel1, pos=wx.Point(272, 232), size=wx.Size(176, 21),
              style=0, value='')

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label='Tinggi', name='staticText8', parent=self.panel1,
              pos=wx.Point(16, 280), size=wx.Size(29, 13), style=0)

        self.txt_tinggi = wx.TextCtrl(id=wxID_FRAME1TXT_TINGGI,
              name='txt_tinggi', parent=self.panel1, pos=wx.Point(104, 280),
              size=wx.Size(100, 21), style=0, value='')

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label='(cm)', name='staticText9', parent=self.panel1,
              pos=wx.Point(216, 283), size=wx.Size(21, 13), style=0)
        self.staticText9.SetForegroundColour(wx.Colour(255, 0, 0))

    def __init__(self, parent):
        self._init_ctrls(parent)
        skrg = datetime.date.today()
        day = skrg.day
        month = skrg.month
        tahun = skrg.year
        displayed = wx.DateTimeFromDMY(day,month-1,tahun)
        displayed.Format("%d/%m/%Y")
        #month1, day1, year1 = tampilan.split('/') 
        #myDate = wx.DateTimeFromDMY(int(day), int(month)-1 , int(year1))
        self.tgl_masuk.SetValue(displayed) 
        self.cmbkategori.Append("Buku")
        self.cmbkategori.Append("Majalah")
        #self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))
        filepath = 'C:\\Gambar\\noimage.jpg'
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        self.gambar.SetBitmap(wx.BitmapFromImage(img))
        self.Isi_List()
    def Isi_Object(self) :
        sql = "select * from buku where kd_buku = '%s' " %(self.txt_kdbuku.GetValue())
        cur.execute(sql)
        if cur.rowcount > 0 :
            hasil = cur.fetchone()
            self.txt_judul.SetValue(hasil[1])
            self.cmbkategori.SetStringSelection(hasil[2])
            if hasil[3] == 0 :
                self.rTidak.Value=True
            else :
                self.rYa.Value = True
            tgl = hasil[4]
            day = tgl.day
            month = tgl.month
            year = tgl.year
            displayed = wx.DateTimeFromDMY(day,month-1,year)
            self.tgl_masuk.SetValue(displayed)
            self.txt_stock.SetValue(str(hasil[5]))
            self.txt_tinggi.SetValue(str(hasil[6]))
            filepath = hasil[7]
            filepath = filepath.replace("\\",'\\\\')
            self.txt_path.SetValue(filepath)
            img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
            self.gambar.SetBitmap(wx.BitmapFromImage(img))  
    def OnTxt_kdbukuTextEnter(self, event):
        self.Isi_Object()

    def OnTmbSimpanButton(self, event):
        sql = "select * from buku where kd_buku='%s' "%(self.txt_kdbuku.GetValue())
        cur.execute(sql)
        judul1 = self.txt_judul.GetValue()
        kategori1 =self.cmbkategori.GetStringSelection()
        if self.rYa.Value == True :
            dipinjam1 = 1
        else :
            dipinjam1 = 0
        selected = self.tgl_masuk.GetValue()
        month = selected.Month + 1
        day = selected.Day
        year = selected.Year
        tgl_masuk1 = datetime.date(year,month,day)
        stock1 = int(self.txt_stock.GetValue())
        tinggi1 = float(self.txt_tinggi.GetValue())
        kd_buku1 =self.txt_kdbuku.GetValue()
        gambar1= self.txt_path.GetValue()
        
        if cur.rowcount > 0 :
                         
            sql = "update buku set judul ='%s', kategori='%s', dipinjam='%d', tgl_masuk='%s', stock ='%d', tinggi='%s',gambar='%s' where kd_buku ='%s' "%(judul1,kategori1,dipinjam1,tgl_masuk1,stock1,tinggi1,gambar1,kd_buku1)
        else :
            sql = "insert into buku (kd_buku,judul,kategori,dipinjam,tgl_masuk,stock,gambar) values ('%s','%s','%s','%d','%s','%d','%s','%s') "%(kd_buku1,judul1,kategori1,dipinjam1,tgl_masuk1,stock1,tinggi1,gambar1)    
        cur.execute(sql)
        conn.commit()
        self.Awal()
    def Awal(self) :
        self.Isi_List()
        self.txt_kdbuku.SetValue("")
        self.txt_judul.SetValue("")
        self.cmbkategori.SetValue("")
        self.rYa.Value=False
        self.rTidak.Value=False
        # mengisi ke DateTimePicker tgl saat ini
        skrg = datetime.date.today()
        day = skrg.day
        month = skrg.month
        tahun = skrg.year
        displayed = wx.DateTimeFromDMY(day,month-1,tahun)
        displayed.Format("%d/%m/%Y")
        self.tgl_masuk.SetValue(displayed) 
        self.txt_stock.SetValue("")
        self.txt_tinggi.SetValue("")
        self.txt_kdbuku.SetFocus()
        ## Kembalikan gambar ke noimage
        filepath = 'C:\\Gambar\\noimage.jpg'
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        self.gambar.SetBitmap(wx.BitmapFromImage(img))
    def Isi_List(self) :
        self.lc.DeleteAllItems()
        sql = "select * from buku order by kd_buku"
        cur.execute(sql)
        hasil = cur.fetchall()
        jumbar = self.lc.GetItemCount()
        for i in hasil :
            self.lc.InsertStringItem(jumbar,i[0])
            self.lc.SetStringItem(jumbar,1,i[1])
            self.lc.SetStringItem(jumbar,2,str(i[5]))
            jumbar = jumbar + 1
    def OnTmbBrowseButton(self, event):
        wildcard = "JPEG files (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.txt_path.SetValue(dialog.GetPath())
        dialog.Destroy() 
        filepath = self.txt_path.GetValue()
        filepath = filepath.replace("\\",'\\\\')
        self.txt_path.SetValue(filepath)
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        self.gambar.SetBitmap(wx.BitmapFromImage(img))  

    def OnLcListItemSelected(self, event):
        a = event.m_itemIndex
        # mengambil no index baris yang dipilih
        b = self.lc.GetItem(a,0).GetText()
        # no index baris dikonversi ke text/ string
        self.txt_kdbuku.SetValue(b)
        self.Isi_Object()

    def OnTmbBersihButton(self, event):
        self.Awal()

    def OnTmbHapusButton(self, event):
        if  self.txt_nim.GetValue()=="" :
            self.pesan = wx.MessageDialog\
            (self,"NIM belum diisi","Konfirmasi",wx.OK)
            self.pesan.ShowModal()
            event.Skip()
        sql = " select * from biodata_radio where nim \
        = '%s'" % (self.txt_nim.GetValue())
        cur.execute(sql)
        hasil= cur.fetchone()
        if cur.rowcount>0 :
            tanya = wx.MessageDialog(self,\
            message="Anda Yakin Hendak Menghapus NIM"\
            +" "+self.txt_nim.GetValue()+" "+\
            "Nama "+self.txt_nama.GetValue()\
            ,style = wx.YES_NO)
            if tanya.ShowModal()==wx.ID_YES:
                sql = "delete from biodata_radio where nim \
                = '%s'" % (self.txt_nim.GetValue())
                cur.execute(sql)
        else :
            self.pesan = wx.MessageDialog(self,\
            "NIM yang akan dihapus tidak terdata\
            di database","Konfirmasi",wx.OK)
            self.pesan.ShowModal()
        self.Awal()
