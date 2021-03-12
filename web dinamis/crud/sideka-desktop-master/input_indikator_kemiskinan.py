import wx
import wx.lib.buttons
import frm_sideka_menu

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GENBITMAPTEXTBUTTON1, 
 wxID_FRAME1GENBITMAPTEXTBUTTON2, wxID_FRAME1STATICBITMAP1, 
 wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, 
 wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TEXTCTRL2, wxID_FRAME1TEXTCTRL3, wxID_FRAME1TEXTCTRL4, 
 wxID_FRAME1TEXTCTRL5, wxID_FRAME1TEXTCTRL6, wxID_FRAME1TEXTCTRL7, 
 wxID_FRAME1TEXTCTRL8, wxID_FRAME1TEXTCTRL9, 
] = [wx.NewId() for _init_ctrls in range(24)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(266, 165), size=wx.Size(911, 445),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Input Indikator Kemiskinan')
        self.SetClientSize(wx.Size(911, 445))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap('png/sideka.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(16, 0),
              size=wx.Size(280, 72), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Input Indikator Kemiskinan', name='staticBox1',
              parent=self, pos=wx.Point(24, 72), size=wx.Size(880, 328),
              style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label=u'1.',
              name='staticText1', parent=self, pos=wx.Point(32, 104),
              size=wx.Size(12, 17), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(48, 104), size=wx.Size(840, 25),
              style=0, value='textCtrl1')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2, label=u'2.',
              name='staticText2', parent=self, pos=wx.Point(32, 136),
              size=wx.Size(12, 17), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(48, 136), size=wx.Size(840, 25),
              style=0, value='textCtrl2')

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3, label=u'3.',
              name='staticText3', parent=self, pos=wx.Point(32, 168),
              size=wx.Size(12, 17), style=0)

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self, pos=wx.Point(48, 168), size=wx.Size(840, 25),
              style=0, value='textCtrl3')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4, label=u'4.',
              name='staticText4', parent=self, pos=wx.Point(32, 200),
              size=wx.Size(12, 17), style=0)

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self, pos=wx.Point(48, 200), size=wx.Size(840, 25),
              style=0, value='textCtrl4')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5, label=u'5.',
              name='staticText5', parent=self, pos=wx.Point(32, 232),
              size=wx.Size(12, 17), style=0)

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL5, name='textCtrl5',
              parent=self, pos=wx.Point(48, 232), size=wx.Size(840, 25),
              style=0, value='textCtrl5')

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6, label=u'6.',
              name='staticText6', parent=self, pos=wx.Point(32, 264),
              size=wx.Size(12, 17), style=0)

        self.textCtrl6 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL6, name='textCtrl6',
              parent=self, pos=wx.Point(48, 264), size=wx.Size(840, 25),
              style=0, value='textCtrl6')

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7, label=u'7.',
              name='staticText7', parent=self, pos=wx.Point(32, 296),
              size=wx.Size(12, 17), style=0)

        self.textCtrl7 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL7, name='textCtrl7',
              parent=self, pos=wx.Point(48, 296), size=wx.Size(840, 25),
              style=0, value='textCtrl7')

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8, label=u'8.',
              name='staticText8', parent=self, pos=wx.Point(32, 328),
              size=wx.Size(12, 17), style=0)

        self.textCtrl8 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL8, name='textCtrl8',
              parent=self, pos=wx.Point(48, 328), size=wx.Size(840, 25),
              style=0, value='textCtrl8')

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9, label=u'9.',
              name='staticText9', parent=self, pos=wx.Point(32, 360),
              size=wx.Size(12, 17), style=0)

        self.textCtrl9 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL9, name='textCtrl9',
              parent=self, pos=wx.Point(48, 360), size=wx.Size(840, 25),
              style=0, value='textCtrl9')

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Keterangan', name='staticBox2', parent=self,
              pos=wx.Point(312, 0), size=wx.Size(592, 80), style=0)

        self.genBitmapTextButton1 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON1, label=u'Simpan Data',
              name='genBitmapTextButton1', parent=self, pos=wx.Point(272, 408),
              size=wx.Size(184, 31), style=0)

        self.genBitmapTextButton2 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON2, label=u'Kembali Ke Menu',
              name='genBitmapTextButton2', parent=self, pos=wx.Point(464, 408),
              size=wx.Size(176, 31), style=0)
        self.genBitmapTextButton2.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton2Button,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON2)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGenBitmapTextButton2Button(self, event):
        self.Close()
        self.main=frm_sideka_menu.create(None)
        self.main.Show()
