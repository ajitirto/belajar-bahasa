#Boa:Frame:Frame1

import wx, MySQLdb

conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="Akademik")
cur = conn.cursor()


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1TMBHAPUS, 
 wxID_FRAME1TXT_NAMA, wxID_FRAME1TXT_NIM, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(387, 245), size=wx.Size(400, 227),
              style=wx.DEFAULT_FRAME_STYLE, title='Menghapus Data Mahasiswa')
        self.SetClientSize(wx.Size(384, 189))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 189),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label='NIM',
              name='staticText1', parent=self.panel1, pos=wx.Point(48, 32),
              size=wx.Size(20, 13), style=0)

        self.txt_nim = wx.TextCtrl(id=wxID_FRAME1TXT_NIM, name='txt_nim',
              parent=self.panel1, pos=wx.Point(104, 32), size=wx.Size(100, 21),
              style=wx.TE_PROCESS_ENTER, value='')
        self.txt_nim.Bind(wx.EVT_TEXT_ENTER, self.OnTxt_nimTextEnter,
              id=wxID_FRAME1TXT_NIM)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Nama', name='staticText2', parent=self.panel1,
              pos=wx.Point(48, 80), size=wx.Size(28, 13), style=0)

        self.txt_nama = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA, name='txt_nama',
              parent=self.panel1, pos=wx.Point(104, 72), size=wx.Size(192, 21),
              style=0, value='')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='(Tekan ENTER)', name='staticText3', parent=self.panel1,
              pos=wx.Point(224, 32), size=wx.Size(82, 13), style=0)
        self.staticText3.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.staticText3.SetForegroundColour(wx.Colour(255, 0, 0))
        self.staticText3.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))

        self.tmbHapus = wx.Button(id=wxID_FRAME1TMBHAPUS, label='Hapus',
              name='tmbHapus', parent=self.panel1, pos=wx.Point(48, 136),
              size=wx.Size(75, 23), style=0)
        self.tmbHapus.Bind(wx.EVT_BUTTON, self.OnTmbHapusButton,
              id=wxID_FRAME1TMBHAPUS)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTmbHapusButton(self, event):
        if  self.txt_nim.GetValue()=="" :
            self.pesan = wx.MessageDialog\
            (self,"NIM belum diisi","Konfirmasi",wx.OK)
            self.pesan.ShowModal()
            event.Skip()
        sql = " select * from mhs where nim \
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
                sql = "delete from mhs where nim \
                = '%s'" % (self.txt_nim.GetValue())
                cur.execute(sql)
        else :
            self.pesan = wx.MessageDialog(self,\
            "NIM yang akan dihapus tidak terdata\
            di database","Konfirmasi",wx.OK)
            self.pesan.ShowModal()
        self.txt_nim.SetValue("")
        self.txt_nama.SetValue("")
        self.txt_nim.SetFocus()

    def OnTxt_nimTextEnter(self, event):
        sql = " select * from mhs where nim \
        = '%s'" %(self.txt_nim.GetValue())
        cur.execute(sql)
        hasil= cur.fetchone()
        if cur.rowcount > 0 :
            self.txt_nama.SetValue(hasil[1])
        else :
            self.pesan = wx.MessageDialog(self,\
            "Data Tidak Ada","Konfirmasi",wx.OK)
            self.pesan.ShowModal()

        

        
        

