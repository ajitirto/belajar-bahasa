import wx
import wx.lib.buttons
import frm_sideka_menu

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GENBITMAPTEXTBUTTON1, 
 wxID_FRAME1GENBITMAPTEXTBUTTON2, wxID_FRAME1GENBITMAPTEXTBUTTON3, 
 wxID_FRAME1GENBITMAPTEXTBUTTON4, wxID_FRAME1STATICBITMAP1, 
 wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
 wxID_FRAME1TEXTCTRL3, wxID_FRAME1TEXTCTRL4, wxID_FRAME1TEXTCTRL5, 
] = [wx.NewId() for _init_ctrls in range(18)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(505, 194), size=wx.Size(326, 501),
              style=wx.FRAME_NO_TASKBAR, title=u'Edit Data Kemiskinan')
        self.SetClientSize(wx.Size(326, 501))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap('png/sideka.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(16, 0),
              size=wx.Size(276, 65), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Cari KK Untuk Edit Data', name='staticBox1', parent=self,
              pos=wx.Point(8, 64), size=wx.Size(304, 120), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Nomor KK', name='staticText1', parent=self,
              pos=wx.Point(24, 88), size=wx.Size(63, 17), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(24, 104), size=wx.Size(272, 25),
              style=0, value=u'')

        self.genBitmapTextButton1 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON1, label=u'Cari Untuk Input',
              name='genBitmapTextButton1', parent=self, pos=wx.Point(152, 136),
              size=wx.Size(144, 31), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Edit Data Kemiskinan', name='staticBox2', parent=self,
              pos=wx.Point(8, 184), size=wx.Size(304, 232), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Nomor KK', name='staticText2', parent=self,
              pos=wx.Point(24, 208), size=wx.Size(63, 17), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(24, 224), size=wx.Size(272, 25),
              style=0, value=u'')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Alamat', name='staticText3', parent=self, pos=wx.Point(24,
              256), size=wx.Size(43, 17), style=0)

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self, pos=wx.Point(24, 272), size=wx.Size(272, 25),
              style=0, value=u'')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Nama Kepala Keluarga', name='staticText4', parent=self,
              pos=wx.Point(24, 304), size=wx.Size(135, 17), style=0)

        self.genBitmapTextButton2 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON2, label=u'Update Data + Edit',
              name='genBitmapTextButton2', parent=self, pos=wx.Point(8, 424),
              size=wx.Size(152, 31), style=0)

        self.genBitmapTextButton3 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON3, label=u'Update Data',
              name='genBitmapTextButton3', parent=self, pos=wx.Point(176, 424),
              size=wx.Size(136, 31), style=0)

        self.genBitmapTextButton4 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON4, label=u'Batal',
              name='genBitmapTextButton4', parent=self, pos=wx.Point(96, 464),
              size=wx.Size(136, 31), style=0)
        self.genBitmapTextButton4.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton4Button,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON4)

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self, pos=wx.Point(24, 320), size=wx.Size(272, 25),
              style=0, value=u'')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Status Kemiskinan', name='staticText5', parent=self,
              pos=wx.Point(24, 352), size=wx.Size(111, 17), style=0)

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL5, name='textCtrl5',
              parent=self, pos=wx.Point(24, 368), size=wx.Size(272, 25),
              style=0, value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGenBitmapTextButton4Button(self, event):
        self.Close()
        self.main=frm_sideka_menu.create(None)
        self.main.Show()

    
