#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1CMEMBACA, wxID_FRAME1CMENULIS, wxID_FRAME1COLAHRAGA, 
 wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1TMBPROSES, wxID_FRAME1TXT_NAMA, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(527, 223), size=wx.Size(400, 278),
              style=wx.DEFAULT_FRAME_STYLE, title='Biodata dengan Hobby')
        self.SetClientSize(wx.Size(384, 240))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 240),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Nama', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 24), size=wx.Size(28, 13), style=0)

        self.txt_nama = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA, name='txt_nama',
              parent=self.panel1, pos=wx.Point(104, 24), size=wx.Size(100, 21),
              style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Hobby', name='staticText2', parent=self.panel1,
              pos=wx.Point(24, 80), size=wx.Size(32, 13), style=0)

        self.cOlahraga = wx.CheckBox(id=wxID_FRAME1COLAHRAGA, label='Olahraga',
              name='cOlahraga', parent=self.panel1, pos=wx.Point(112, 80),
              size=wx.Size(70, 13), style=0)
        self.cOlahraga.SetValue(False)
        self.cOlahraga.Bind(wx.EVT_CHECKBOX, self.OnCOlahragaCheckbox,
              id=wxID_FRAME1COLAHRAGA)

        self.cMembaca = wx.CheckBox(id=wxID_FRAME1CMEMBACA, label='Membaca',
              name='cMembaca', parent=self.panel1, pos=wx.Point(112, 112),
              size=wx.Size(70, 13), style=0)
        self.cMembaca.SetValue(False)

        self.cMenulis = wx.CheckBox(id=wxID_FRAME1CMENULIS, label='Menulis',
              name='cMenulis', parent=self.panel1, pos=wx.Point(112, 144),
              size=wx.Size(70, 13), style=0)
        self.cMenulis.SetValue(False)

        self.tmbProses = wx.Button(id=wxID_FRAME1TMBPROSES, label='Proses',
              name='tmbProses', parent=self.panel1, pos=wx.Point(120, 192),
              size=wx.Size(75, 23), style=0)
        self.tmbProses.Bind(wx.EVT_BUTTON, self.OnTmbProsesButton,
              id=wxID_FRAME1TMBPROSES)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTmbProsesButton(self, event):
        nama  = self.txt_nama.GetValue()
        if self.cOlahraga.GetValue()== True :
            olahraga = "Ya"
        else :
            olahraga ="Tidak"
        if self.cMembaca.GetValue()==True :
            membaca = "Ya"
        else :
            membaca = "Tidak"
        if self.cMenulis.GetValue()==True :
            menulis ="Ya"
        else :
            menulis ="Tidak"
        pesan1 = "Nama : "+nama+"\n"\
        + "Hobby : "+"\n"\
        + "Olahraga : "+olahraga\
        +"\n"+ "Membaca : " + membaca\
        +"\n"+ "Menulis : " + menulis
        self.pesan = wx.MessageDialog(self,\
            pesan1,"PESAN",wx.OK)
        self.pesan.ShowModal()

    def OnCOlahragaCheckbox(self, event):
        event.Skip()
        
