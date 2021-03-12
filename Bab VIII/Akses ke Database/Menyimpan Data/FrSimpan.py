#Boa:Frame:Frame1

import wx, MySQLdb

conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="Akademik")
cur = conn.cursor()

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1TMBSIMPAN, wxID_FRAME1TXT_NAMA, 
 wxID_FRAME1TXT_NIM, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(493, 238), size=wx.Size(400, 218),
              style=wx.DEFAULT_FRAME_STYLE, title='Menyimpan Data Mahasiswa')
        self.SetClientSize(wx.Size(384, 180))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 180),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(214, 214, 214))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label='NIM',
              name='staticText1', parent=self.panel1, pos=wx.Point(32, 32),
              size=wx.Size(20, 13), style=0)

        self.txt_nim = wx.TextCtrl(id=wxID_FRAME1TXT_NIM, name='txt_nim',
              parent=self.panel1, pos=wx.Point(96, 32), size=wx.Size(100, 21),
              style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Nama', name='staticText2', parent=self.panel1,
              pos=wx.Point(32, 80), size=wx.Size(28, 13), style=0)

        self.txt_nama = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA, name='txt_nama',
              parent=self.panel1, pos=wx.Point(96, 80), size=wx.Size(184, 21),
              style=0, value='')

        self.tmbSimpan = wx.Button(id=wxID_FRAME1TMBSIMPAN, label='Simpan',
              name='tmbSimpan', parent=self.panel1, pos=wx.Point(32, 136),
              size=wx.Size(75, 23), style=0)
        self.tmbSimpan.Bind(wx.EVT_BUTTON, self.OnTmbSimpanButton,
              id=wxID_FRAME1TMBSIMPAN)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTmbSimpanButton(self, event):
        sql = "insert into mhs values \
        ('%s','%s')" %(self.txt_nim.GetValue(),\
        self.txt_nama.GetValue())
        cur.execute(sql)
        conn.commit()
        self.txt_nim.SetValue("")
        self.txt_nama.SetValue("")
        self.txt_nim.SetFocus()

