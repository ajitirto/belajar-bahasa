#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1TH_LAHIR, 
 wxID_FRAME1TXT_USIA, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(585, 231), size=wx.Size(361, 216),
              style=wx.DEFAULT_FRAME_STYLE, title='Hitung Usia')
        self.SetClientSize(wx.Size(345, 178))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(345, 178),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(223, 223, 223))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Tahun Lahir', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 32), size=wx.Size(57, 13), style=0)

        self.th_lahir = wx.TextCtrl(id=wxID_FRAME1TH_LAHIR, name='th_lahir',
              parent=self.panel1, pos=wx.Point(120, 32), size=wx.Size(100, 21),
              style=wx.TE_PROCESS_ENTER, value='')
        self.th_lahir.Bind(wx.EVT_TEXT_ENTER, self.OnTh_lahirTextEnter,
              id=wxID_FRAME1TH_LAHIR)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Usia', name='staticText2', parent=self.panel1,
              pos=wx.Point(24, 88), size=wx.Size(21, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='(TEKAN ENTER)', name='staticText3', parent=self.panel1,
              pos=wx.Point(232, 32), size=wx.Size(75, 13), style=0)
        self.staticText3.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))
        self.staticText3.SetForegroundColour(wx.Colour(255, 0, 0))

        self.txt_usia = wx.TextCtrl(id=wxID_FRAME1TXT_USIA, name='txt_usia',
              parent=self.panel1, pos=wx.Point(120, 88), size=wx.Size(100, 21),
              style=0, value='')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTh_lahirTextEnter(self, event):
        Usia = 2012 - int(self.th_lahir.GetValue())
        self.txt_usia.SetValue(str(Usia))
        if Usia >=0 and Usia<=5 :
            self.pesan = wx.MessageDialog(self,\
            "BALITA","KATEGORI",wx.OK)
        elif Usia >=6 and Usia<=12 :
            self.pesan = wx.MessageDialog(self,\
            "ANAK-ANAK","KATEGORI",wx.OK)
        elif Usia >=13 and Usia<=17 :
            self.pesan = wx.MessageDialog(self,\
            "REMAJA","KATEGORI",wx.OK)
        elif Usia >=18 and Usia<=50 :
            self.pesan = wx.MessageDialog(self,\
            "DEWASA","KATEGORI",wx.OK)
        else :
            self.pesan = wx.MessageDialog(self,\
            "LANSIA","KATEGORI",wx.OK)
        self.pesan.ShowModal()
        

   
