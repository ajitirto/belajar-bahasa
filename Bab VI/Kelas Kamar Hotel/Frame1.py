#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1CMBKELAS, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1TXT_TARIF, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(465, 204), size=wx.Size(400, 231),
              style=wx.DEFAULT_FRAME_STYLE, title='Tarif Kelas Kamar')
        self.SetClientSize(wx.Size(384, 193))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 193),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(193, 193, 193))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Kelas Kamar', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 40), size=wx.Size(59, 13), style=0)

        self.cmbKelas = wx.ComboBox(choices=['EXECUTIVE', 'STANDARD', 'FAMILY'],
              id=wxID_FRAME1CMBKELAS, name='cmbKelas', parent=self.panel1,
              pos=wx.Point(136, 40), size=wx.Size(130, 21), style=0, value='')
        self.cmbKelas.SetLabel('')
        self.cmbKelas.Bind(wx.EVT_COMBOBOX, self.OnCmbKelasCombobox,
              id=wxID_FRAME1CMBKELAS)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Tarif', name='staticText2', parent=self.panel1,
              pos=wx.Point(24, 104), size=wx.Size(24, 13), style=0)

        self.txt_tarif = wx.TextCtrl(id=wxID_FRAME1TXT_TARIF, name='txt_tarif',
              parent=self.panel1, pos=wx.Point(136, 104), size=wx.Size(128, 21),
              style=0, value='')

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def OnCmbKelasCombobox(self, event):
        pil = self.cmbKelas.GetStringSelection()
        if pil=="EXECUTIVE" :
            self.txt_tarif.SetValue("650000")
        elif pil=="STANDARD" :
            self.txt_tarif.SetValue("350000")
        else :
            self.txt_tarif.SetValue("250000")
