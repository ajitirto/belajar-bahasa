#Boa:Frame:Frame1

import wx, MySQLdb

conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="akses_database")
cur = conn.cursor()

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1TMB_BERSIH, 
 wxID_FRAME1TMB_HAPUS, wxID_FRAME1TMB_SIMPAN, wxID_FRAME1TXT_IPK, 
 wxID_FRAME1TXT_NAMA, wxID_FRAME1TXT_NIM, 
] = [wx.NewId() for _init_ctrls in range(11)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(562, 248), size=wx.Size(400, 271),
              style=wx.DEFAULT_FRAME_STYLE, title='Operasi Numerik Desimal')
        self.SetClientSize(wx.Size(384, 233))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 233),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label='NIM',
              name='staticText1', parent=self.panel1, pos=wx.Point(32, 32),
              size=wx.Size(20, 13), style=0)

        self.txt_nim = wx.TextCtrl(id=wxID_FRAME1TXT_NIM, name='txt_nim',
              parent=self.panel1, pos=wx.Point(120, 32), size=wx.Size(100, 21),
              style=wx.TE_PROCESS_ENTER, value='')
        self.txt_nim.Bind(wx.EVT_TEXT_ENTER, self.OnTxt_nimTextEnter,
              id=wxID_FRAME1TXT_NIM)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Nama', name='staticText2', parent=self.panel1,
              pos=wx.Point(32, 88), size=wx.Size(28, 13), style=0)

        self.txt_nama = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA, name='txt_nama',
              parent=self.panel1, pos=wx.Point(120, 80), size=wx.Size(184, 21),
              style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3, label='IPK',
              name='staticText3', parent=self.panel1, pos=wx.Point(32, 144),
              size=wx.Size(17, 13), style=0)

        self.txt_ipk = wx.TextCtrl(id=wxID_FRAME1TXT_IPK, name='txt_ipk',
              parent=self.panel1, pos=wx.Point(120, 136), size=wx.Size(100, 21),
              style=0, value='')

        self.tmb_Simpan = wx.Button(id=wxID_FRAME1TMB_SIMPAN, label='Simpan',
              name='tmb_Simpan', parent=self.panel1, pos=wx.Point(32, 192),
              size=wx.Size(75, 23), style=0)
        self.tmb_Simpan.Bind(wx.EVT_BUTTON, self.OnTmb_SimpanButton,
              id=wxID_FRAME1TMB_SIMPAN)

        self.tmb_Bersih = wx.Button(id=wxID_FRAME1TMB_BERSIH, label='Bersih',
              name='tmb_Bersih', parent=self.panel1, pos=wx.Point(136, 192),
              size=wx.Size(75, 23), style=0)
        self.tmb_Bersih.Bind(wx.EVT_BUTTON, self.OnTmb_BersihButton,
              id=wxID_FRAME1TMB_BERSIH)

        self.tmb_Hapus = wx.Button(id=wxID_FRAME1TMB_HAPUS, label='Hapus',
              name='tmb_Hapus', parent=self.panel1, pos=wx.Point(240, 192),
              size=wx.Size(75, 23), style=0)
        self.tmb_Hapus.Bind(wx.EVT_BUTTON, self.OnTmb_HapusButton,
              id=wxID_FRAME1TMB_HAPUS)

    def __init__(self, parent):
        self._init_ctrls(parent)
    
    def Bersih (self) :
        self.txt_nim.SetValue("")
        self.txt_nama.SetValue("")
        self.txt_ipk.SetValue("")
        self.txt_nim.SetFocus()

    def OnTmb_SimpanButton(self, event):
        sql = " select * from ipk where nim \
        = '%s'" %(self.txt_nim.GetValue())
        cur.execute(sql)
        hasil= cur.fetchone()
        ipk1 = float(self.txt_ipk.GetValue())
        if cur.rowcount > 0 :
            sql =" update ipk set nama =\
            '%s', ipk='%s' where nim ='%s'"%\
            (self.txt_nama.GetValue(),\
            ipk1,self.txt_nim.GetValue())
        else :
            sql ="insert into ipk (nim,nama,ipk) \
            values ('%s','%s','%s')"%(self.txt_nim.GetValue(),\
            self.txt_nama.GetValue(),ipk1)
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
        sql = " select * from ipk where nim \
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
                sql = "delete from ipk where nim \
                = '%s'" % (self.txt_nim.GetValue())
                cur.execute(sql)
        else :
            self.pesan = wx.MessageDialog(self,\
            "NIM yang akan dihapus tidak terdata\
            di database","Konfirmasi",wx.OK)
            self.pesan.ShowModal()

    def OnTxt_nimTextEnter(self, event):
        sql = " select * from ipk where nim \
        = '%s'" %(self.txt_nim.GetValue())
        cur.execute(sql)
        hasil= cur.fetchone()
        if cur.rowcount > 0 :
            self.txt_nama.SetValue(hasil[1])
            self.txt_ipk.SetValue(str(hasil[2]))
        else :
            self.pesan = wx.MessageDialog(self,\
            "Data Tidak Ada","Konfirmasi",wx.OK)
            self.pesan.ShowModal()
