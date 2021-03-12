#Boa:Frame:Frame1

import wx, MySQLdb
conn= MySQLdb.connect(host="localhost", user="root", passwd="",db="akses_database")
cur = conn.cursor()


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GAMBAR, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1TMB_BERSIH, wxID_FRAME1TMB_BROWSE, 
 wxID_FRAME1TMB_HAPUS, wxID_FRAME1TMB_SIMPAN, wxID_FRAME1TXT_JUDUL, 
 wxID_FRAME1TXT_KD_BUKU, wxID_FRAME1TXT_PATH, wxID_FRAME1TXT_PENERBIT, 
 wxID_FRAME1TXT_PENULIS, 
] = [wx.NewId() for _init_ctrls in range(17)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(483, 244), size=wx.Size(473, 308),
              style=wx.DEFAULT_FRAME_STYLE, title='Penggunaan Gambar')
        self.SetClientSize(wx.Size(457, 270))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(457, 270),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Kode Buku', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 32), size=wx.Size(51, 13), style=0)

        self.txt_kd_buku = wx.TextCtrl(id=wxID_FRAME1TXT_KD_BUKU,
              name='txt_kd_buku', parent=self.panel1, pos=wx.Point(112, 32),
              size=wx.Size(100, 21), style=wx.TE_PROCESS_ENTER, value='')
        self.txt_kd_buku.Bind(wx.EVT_TEXT_ENTER, self.OnTxt_kd_bukuTextEnter,
              id=wxID_FRAME1TXT_KD_BUKU)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Judul', name='staticText2', parent=self.panel1,
              pos=wx.Point(24, 88), size=wx.Size(25, 13), style=0)

        self.txt_judul = wx.TextCtrl(id=wxID_FRAME1TXT_JUDUL, name='txt_judul',
              parent=self.panel1, pos=wx.Point(112, 88), size=wx.Size(176, 21),
              style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Penulis', name='staticText3', parent=self.panel1,
              pos=wx.Point(24, 144), size=wx.Size(34, 13), style=0)

        self.txt_penulis = wx.TextCtrl(id=wxID_FRAME1TXT_PENULIS,
              name='txt_penulis', parent=self.panel1, pos=wx.Point(112, 136),
              size=wx.Size(176, 21), style=0, value='')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label='Penerbit', name='staticText4', parent=self.panel1,
              pos=wx.Point(24, 192), size=wx.Size(41, 13), style=0)

        self.txt_penerbit = wx.TextCtrl(id=wxID_FRAME1TXT_PENERBIT,
              name='txt_penerbit', parent=self.panel1, pos=wx.Point(116, 184),
              size=wx.Size(172, 21), style=0, value='')

        self.gambar = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GAMBAR, name='gambar', parent=self.panel1,
              pos=wx.Point(320, 32), size=wx.Size(104, 112), style=0)

        self.tmb_Simpan = wx.Button(id=wxID_FRAME1TMB_SIMPAN, label='Simpan',
              name='tmb_Simpan', parent=self.panel1, pos=wx.Point(24, 232),
              size=wx.Size(75, 23), style=0)
        self.tmb_Simpan.Bind(wx.EVT_BUTTON, self.OnTmb_SimpanButton,
              id=wxID_FRAME1TMB_SIMPAN)

        self.tmb_Bersih = wx.Button(id=wxID_FRAME1TMB_BERSIH, label='Bersih',
              name='tmb_Bersih', parent=self.panel1, pos=wx.Point(152, 232),
              size=wx.Size(75, 23), style=0)
        self.tmb_Bersih.Bind(wx.EVT_BUTTON, self.OnTmb_BersihButton,
              id=wxID_FRAME1TMB_BERSIH)

        self.tmb_Hapus = wx.Button(id=wxID_FRAME1TMB_HAPUS, label='Hapus',
              name='tmb_Hapus', parent=self.panel1, pos=wx.Point(288, 232),
              size=wx.Size(75, 23), style=0)
        self.tmb_Hapus.Bind(wx.EVT_BUTTON, self.OnTmb_HapusButton,
              id=wxID_FRAME1TMB_HAPUS)

        self.tmb_Browse = wx.Button(id=wxID_FRAME1TMB_BROWSE, label='Browse',
              name='tmb_Browse', parent=self.panel1, pos=wx.Point(320, 160),
              size=wx.Size(104, 23), style=0)
        self.tmb_Browse.Bind(wx.EVT_BUTTON, self.OnTmb_BrowseButton,
              id=wxID_FRAME1TMB_BROWSE)

        self.txt_path = wx.TextCtrl(id=wxID_FRAME1TXT_PATH, name='txt_path',
              parent=self.panel1, pos=wx.Point(304, 192), size=wx.Size(136, 21),
              style=0, value='')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label='(Enter)', name='staticText5', parent=self.panel1,
              pos=wx.Point(224, 32), size=wx.Size(40, 13), style=0)
        self.staticText5.SetForegroundColour(wx.Colour(255, 0, 0))
        self.staticText5.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)
        filepath = 'C:\\Gambar\\noimage.jpg'
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        self.gambar.SetBitmap(wx.BitmapFromImage(img))
        
    def Isi_Object(self) :
        sql = "select * from buku_gambar where kd_buku = '%s' "\
         %(self.txt_kd_buku.GetValue())
        cur.execute(sql)
        if cur.rowcount > 0 :
            hasil = cur.fetchone()
            self.txt_judul.SetValue(hasil[1])
            self.txt_penulis.SetValue(hasil[2])
            self.txt_penerbit.SetValue(hasil[3])
            filepath = hasil[4]
            filepath = filepath.replace("\\",'\\\\')
            self.txt_path.SetValue(filepath)
            img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
            self.gambar.SetBitmap(wx.BitmapFromImage(img))  
    
    def Awal(self) :
        self.txt_kd_buku.SetValue("")
        self.txt_judul.SetValue("")
        self.txt_penulis.SetValue("")
        self.txt_penerbit.SetValue("")
        self.txt_path.SetValue("")
        self.txt_kd_buku.SetFocus()
        ## Mengisi StaticBitmap gambar dengan tampilan noimage
        filepath = 'C:\\Gambar\\noimage.jpg'
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        self.gambar.SetBitmap(wx.BitmapFromImage(img))
    
    def OnTxt_kd_bukuTextEnter(self, event):
        self.Isi_Object()

    def OnTmb_SimpanButton(self, event):
        sql = "select * from buku_gambar where kd_buku='%s' "%\
        (self.txt_kd_buku.GetValue())
        cur.execute(sql)
        judul1 = self.txt_judul.GetValue()
        penulis1 = self.txt_penulis.GetValue()
        penerbit1= self.txt_penerbit.GetValue()
        kd_buku1 =self.txt_kd_buku.GetValue()
        gambar1= self.txt_path.GetValue()
        
        if cur.rowcount > 0 :
                         
            sql = "update buku_gambar set judul ='%s',penulis='%s',penerbit='%s', gambar='%s' where \
            kd_buku ='%s' "%(judul1,penulis1,penerbit1,gambar1,kd_buku1)
        else :
            sql = "insert into buku_gambar (kd_buku,judul,penulis,penerbit,gambar) \
            values ('%s','%s','%s','%s','%s') "%\
            (kd_buku1,judul1,penulis1,penerbit1,gambar1)    
            # Collation di MySQL diganti ke latin1_swedish_ci
        cur.execute(sql)
        conn.commit()
        self.Awal()
    def OnTmb_BersihButton(self, event):
        self.Awal()

    def OnTmb_HapusButton(self, event):
        if  self.txt_kd_buku.GetValue()=="" :
            self.pesan = wx.MessageDialog\
            (self,"Kode Buku belum diisi","Konfirmasi",wx.OK)
            self.pesan.ShowModal()
            event.Skip()
        sql = " select * from buku_gambar where kd_buku \
        = '%s'" % (self.txt_kd_buku.GetValue())
        cur.execute(sql)
        hasil= cur.fetchone()
        if cur.rowcount>0 :
            tanya = wx.MessageDialog(self,\
            message="Anda Yakin Hendak Menghapus Kode Buku"\
            +" "+self.txt_kd_buku.GetValue()+" "+\
            "Judul "+self.txt_judul.GetValue()\
            ,style = wx.YES_NO)
            if tanya.ShowModal()==wx.ID_YES:
                sql = "delete from buku_gambar where kd_buku \
                = '%s'" % (self.txt_kd_buku.GetValue())
                cur.execute(sql)
        else :
            self.pesan = wx.MessageDialog(self,\
            "Kode Buku yang akan dihapus tidak terdata\
            di database","Konfirmasi",wx.OK)
            self.pesan.ShowModal()
        self.Awal()

    def OnTmb_BrowseButton(self, event):
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

    
