#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1RPRIA, wxID_FRAME1RWANITA, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1TMBPROSES, 
 wxID_FRAME1TXT_NAMA, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(564, 216), size=wx.Size(400, 228),
              style=wx.DEFAULT_FRAME_STYLE, title='Biodata')
        self.SetClientSize(wx.Size(384, 190))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 190),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Nama', name='staticText1', parent=self.panel1,
              pos=wx.Point(32, 32), size=wx.Size(28, 13), style=0)

        self.txt_nama = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA, name='txt_nama',
              parent=self.panel1, pos=wx.Point(128, 32), size=wx.Size(100, 21),
              style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Jenis Kelamin', name='staticText2', parent=self.panel1,
              pos=wx.Point(32, 88), size=wx.Size(63, 13), style=0)

        self.rPria = wx.RadioButton(id=wxID_FRAME1RPRIA, label='Pria',
              name='rPria', parent=self.panel1, pos=wx.Point(136, 88),
              size=wx.Size(81, 13), style=0)
        self.rPria.SetValue(False)

        self.rWanita = wx.RadioButton(id=wxID_FRAME1RWANITA, label='Wanita',
              name='rWanita', parent=self.panel1, pos=wx.Point(256, 88),
              size=wx.Size(81, 13), style=0)
        self.rWanita.SetValue(False)

        self.tmbProses = wx.Button(id=wxID_FRAME1TMBPROSES, label='Proses',
              name='tmbProses', parent=self.panel1, pos=wx.Point(136, 128),
              size=wx.Size(75, 23), style=0)
        self.tmbProses.Bind(wx.EVT_BUTTON, self.OnTmbProsesButton,
              id=wxID_FRAME1TMBPROSES)

    def __init__(self, parent):
        self._init_ctrls(parent)
        

    def OnTmbProsesButton(self, event):
        nama = self.txt_nama.GetValue()
        if self.rPria.GetValue()==True :
            jk = "Pria"
        else :
            jk ="Wanita"
        a = "Nama : "+nama+" "+"Jenis Kelamin : "+" "+jk
        self.pesan = wx.MessageDialog(self,\
            a,"PESAN",wx.OK)
        self.pesan.ShowModal()
            
