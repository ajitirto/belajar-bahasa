#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1CMBPENDIDIKAN, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1TXT_NAMA, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(614, 225), size=wx.Size(402, 264),
              style=wx.DEFAULT_FRAME_STYLE, title='Biodata dengan Combo')
        self.SetClientSize(wx.Size(386, 226))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(386, 226),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(211, 211, 211))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Nama', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 24), size=wx.Size(28, 13), style=0)

        self.txt_nama = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA, name='txt_nama',
              parent=self.panel1, pos=wx.Point(120, 24), size=wx.Size(100, 21),
              style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Pendidikan', name='staticText2', parent=self.panel1,
              pos=wx.Point(24, 88), size=wx.Size(52, 13), style=0)

        self.cmbPendidikan = wx.ComboBox(choices=[],
              id=wxID_FRAME1CMBPENDIDIKAN, name='cmbPendidikan',
              parent=self.panel1, pos=wx.Point(120, 88), size=wx.Size(130, 21),
              style=0, value='')
        self.cmbPendidikan.SetLabel('')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label='Proses',
              name='button1', parent=self.panel1, pos=wx.Point(136, 160),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.cmbPendidikan.Append("SD")
        self.cmbPendidikan.Append("SMP")
        self.cmbPendidikan.Append("SMA")
        self.cmbPendidikan.Append("S1")
        
        
    def OnButton1Button(self, event):
        nama = self.txt_nama.GetValue()
        pnd = self.cmbPendidikan.GetStringSelection()
        a = "Nama : " + nama +" \n"+\
        " Pendidikan : " + pnd
        self.pesan = wx.MessageDialog(self,\
            a,"PESAN",wx.OK)
        self.pesan.ShowModal()
        

