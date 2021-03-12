#Boa:Frame:Frame1

import wx, MySQLdb

conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="akses_database")
cur = conn.cursor()

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1RLAKI, wxID_FRAME1RWANITA, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1TMB_BERSIH, wxID_FRAME1TMB_HAPUS, 
 wxID_FRAME1TMB_SIMPAN, wxID_FRAME1TXT_NAMA, wxID_FRAME1TXT_NIM, 
] = [wx.NewId() for _init_ctrls in range(13)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(866, 259), size=wx.Size(400, 337),
              style=wx.DEFAULT_FRAME_STYLE,
              title='Biodata Database dengan RadioButton')
        self.SetClientSize(wx.Size(384, 299))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 299),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label='NIM',
              name='staticText1', parent=self.panel1, pos=wx.Point(24, 40),
              size=wx.Size(20, 13), style=0)

        self.txt_nim = wx.TextCtrl(id=wxID_FRAME1TXT_NIM, name='txt_nim',
              parent=self.panel1, pos=wx.Point(120, 40), size=wx.Size(100, 21),
              style=wx.TE_PROCESS_ENTER, value='')
        self.txt_nim.Bind(wx.EVT_TEXT_ENTER, self.OnTxt_nimTextEnter,
              id=wxID_FRAME1TXT_NIM)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Nama', name='staticText2', parent=self.panel1,
              pos=wx.Point(24, 96), size=wx.Size(28, 13), style=0)

        self.txt_nama = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA, name='txt_nama',
              parent=self.panel1, pos=wx.Point(120, 96), size=wx.Size(200, 21),
              style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Jenis Kelamin', name='staticText3', parent=self.panel1,
              pos=wx.Point(24, 168), size=wx.Size(63, 13), style=0)

        self.rLaki = wx.RadioButton(id=wxID_FRAME1RLAKI, label='Laki-laki',
              name='rLaki', parent=self.panel1, pos=wx.Point(112, 168),
              size=wx.Size(81, 13), style=0)
        self.rLaki.SetValue(True)

        self.rWanita = wx.RadioButton(id=wxID_FRAME1RWANITA, label='Wanita',
              name='rWanita', parent=self.panel1, pos=wx.Point(232, 168),
              size=wx.Size(81, 13), style=0)
        self.rWanita.SetValue(False)

        self.tmb_Simpan = wx.Button(id=wxID_FRAME1TMB_SIMPAN, label='Simpan',
              name='tmb_Simpan', parent=self.panel1, pos=wx.Point(24, 216),
              size=wx.Size(75, 23), style=0)
        self.tmb_Simpan.Bind(wx.EVT_BUTTON, self.OnTmb_SimpanButton,
              id=wxID_FRAME1TMB_SIMPAN)

        self.tmb_Bersih = wx.Button(id=wxID_FRAME1TMB_BERSIH, label='Bersih',
              name='tmb_Bersih', parent=self.panel1, pos=wx.Point(144, 216),
              size=wx.Size(75, 23), style=0)
        self.tmb_Bersih.Bind(wx.EVT_BUTTON, self.OnTmb_BersihButton,
              id=wxID_FRAME1TMB_BERSIH)

        self.tmb_Hapus = wx.Button(id=wxID_FRAME1TMB_HAPUS, label='Hapus',
              name='tmb_Hapus', parent=self.panel1, pos=wx.Point(248, 216),
              size=wx.Size(75, 23), style=0)
        self.tmb_Hapus.Bind(wx.EVT_BUTTON, self.OnTmb_HapusButton,
              id=wxID_FRAME1TMB_HAPUS)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label='(ENTER)', name='staticText4', parent=self.panel1,
              pos=wx.Point(240, 43), size=wx.Size(44, 13), style=0)
        self.staticText4.SetForegroundColour(wx.Colour(255, 0, 0))
        self.staticText4.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)
    def Bersih(self) :
        self.txt_nim.SetValue("")
        self.txt_nama.SetValue("")
        self.rLaki.SetValue(False)
        self.rWanita.SetValue(False)
        self.txt_nim.SetFocus()


    def OnTxt_nimTextEnter(self, event):
        sql = " select * from biodata_radio where nim \
        = '%s'" %(self.txt_nim.GetValue())
        cur.execute(sql)
        hasil= cur.fetchone()
        if cur.rowcount > 0 :
            self.txt_nama.SetValue(hasil[1])
            if hasil[2]=="L" :
                self.rLaki.SetValue(True)
            else :
                self.rWanita.SetValue(True)
        else :
            self.pesan = wx.MessageDialog(self,\
            "Data Tidak Ada","Konfirmasi",wx.OK)
            self.pesan.ShowModal()


    def OnTmb_SimpanButton(self, event):
        sql = " select * from biodata_radio where nim \
        = '%s'" %(self.txt_nim.GetValue())
        cur.execute(sql)
        hasil= cur.fetchone()
        if self.rLaki.GetValue()== True :
            jkl = "L"
        else :
            jkl = "P"
        if cur.rowcount > 0 :
            sql =" update biodata_radio set nama =\
            '%s', jns_klm='%s' where nim ='%s'"%\
            (self.txt_nama.GetValue(),\
            jkl,self.txt_nim.GetValue())
        else :
            sql ="insert into biodata_radio (nim,nama,jns_klm) \
            values ('%s','%s','%s')"%(self.txt_nim.GetValue(),\
            self.txt_nama.GetValue(),jkl)
        cur.execute(sql)
        self.Bersih()


    def OnTmb_BersihButton(self, event):
        self.Bersih()

    def OnTmb_HapusButton(self, event):
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

