#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1TMBPROSES, wxID_FRAME1TXT_NAMA1, 
 wxID_FRAME1TXT_NAMA2, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(561, 157), size=wx.Size(400, 241),
              style=wx.DEFAULT_FRAME_STYLE, title='Latihan Menampilkan Nama')
        self.SetClientSize(wx.Size(384, 203))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 203),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Masukkan Nama', name='staticText1', parent=self.panel1,
              pos=wx.Point(32, 40), size=wx.Size(78, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Namanya adalah', name='staticText2', parent=self.panel1,
              pos=wx.Point(32, 104), size=wx.Size(81, 13), style=0)

        self.txt_Nama1 = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA1, name='txt_Nama1',
              parent=self.panel1, pos=wx.Point(144, 40), size=wx.Size(100, 21),
              style=0, value='')

        self.txt_Nama2 = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA2, name='txt_Nama2',
              parent=self.panel1, pos=wx.Point(144, 104), size=wx.Size(100, 21),
              style=0, value='')

        self.tmbProses = wx.Button(id=wxID_FRAME1TMBPROSES, label='Proses',
              name='tmbProses', parent=self.panel1, pos=wx.Point(272, 40),
              size=wx.Size(75, 23), style=0)
        self.tmbProses.Bind(wx.EVT_BUTTON, self.OnTmbProsesButton,
              id=wxID_FRAME1TMBPROSES)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTmbProsesButton(self, event):
        nama = self.txt_Nama1.GetValue()
        self.txt_Nama2.SetValue(nama)
        