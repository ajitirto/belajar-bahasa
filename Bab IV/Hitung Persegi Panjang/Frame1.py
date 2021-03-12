#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1TMBHITUNG, 
 wxID_FRAME1TXT_LEBAR, wxID_FRAME1TXT_LUAS, wxID_FRAME1TXT_PANJANG, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(526, 258), size=wx.Size(341, 257),
              style=wx.DEFAULT_FRAME_STYLE, title='Menghitung Luas Persegi')
        self.SetClientSize(wx.Size(325, 219))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(306, 219),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Panjang', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 24), size=wx.Size(40, 13), style=0)

        self.txt_panjang = wx.TextCtrl(id=wxID_FRAME1TXT_PANJANG,
              name='txt_panjang', parent=self.panel1, pos=wx.Point(120, 24),
              size=wx.Size(100, 21), style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Lebar', name='staticText2', parent=self.panel1,
              pos=wx.Point(24, 64), size=wx.Size(28, 13), style=0)

        self.txt_lebar = wx.TextCtrl(id=wxID_FRAME1TXT_LEBAR, name='txt_lebar',
              parent=self.panel1, pos=wx.Point(120, 64), size=wx.Size(100, 21),
              style=0, value='')

        self.tmbHitung = wx.Button(id=wxID_FRAME1TMBHITUNG, label='Hitung Luas',
              name='tmbHitung', parent=self.panel1, pos=wx.Point(128, 112),
              size=wx.Size(75, 23), style=0)
        self.tmbHitung.Bind(wx.EVT_BUTTON, self.OnTmbHitungButton,
              id=wxID_FRAME1TMBHITUNG)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Luas', name='staticText3', parent=self.panel1,
              pos=wx.Point(24, 168), size=wx.Size(23, 13), style=0)

        self.txt_luas = wx.TextCtrl(id=wxID_FRAME1TXT_LUAS, name='txt_luas',
              parent=self.panel1, pos=wx.Point(120, 160), size=wx.Size(100, 21),
              style=0, value='')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTmbHitungButton(self, event):
        p = int(self.txt_panjang.GetValue())
        l = int(self.txt_lebar.GetValue())
        luas = p * l
        self.txt_luas.SetValue(str(luas))
        
