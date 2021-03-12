#Boa:Frame:Frame1

import wx, MySQLdb

conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="Akademik")
cur = conn.cursor()

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1TMBCARI, wxID_FRAME1TXT_NAMA, 
 wxID_FRAME1TXT_NIM, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(600, 242), size=wx.Size(400, 181),
              style=wx.DEFAULT_FRAME_STYLE, title='Cari Data Mahasiswa')
        self.SetClientSize(wx.Size(384, 143))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 143),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(211, 211, 211))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label='NIM',
              name='staticText1', parent=self.panel1, pos=wx.Point(32, 32),
              size=wx.Size(20, 13), style=0)

        self.txt_nim = wx.TextCtrl(id=wxID_FRAME1TXT_NIM, name='txt_nim',
              parent=self.panel1, pos=wx.Point(128, 32), size=wx.Size(100, 21),
              style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Nama', name='staticText2', parent=self.panel1,
              pos=wx.Point(32, 80), size=wx.Size(28, 13), style=0)

        self.txt_nama = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA, name='txt_nama',
              parent=self.panel1, pos=wx.Point(128, 80), size=wx.Size(192, 21),
              style=0, value='')

        self.tmbCari = wx.Button(id=wxID_FRAME1TMBCARI, label='Cari',
              name='tmbCari', parent=self.panel1, pos=wx.Point(248, 32),
              size=wx.Size(75, 23), style=0)
        self.tmbCari.Bind(wx.EVT_BUTTON, self.OnTmbCariButton,
              id=wxID_FRAME1TMBCARI)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTmbCariButton(self, event):
        sql = " select * from mhs where nim = '%s'" %(self.txt_nim.GetValue())
        cur.execute(sql)
        hasil= cur.fetchone()
        if cur.rowcount > 0 :
            self.txt_nama.SetValue(hasil[1])
        else :
            self.pesan = wx.MessageDialog(self,"Data Tidak Ada","Konfirmasi",wx.OK)
            self.pesan.ShowModal()

