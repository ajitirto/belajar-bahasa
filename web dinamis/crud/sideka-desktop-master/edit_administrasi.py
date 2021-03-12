import wx
import wx.lib.buttons

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GENBITMAPTEXTBUTTON1, 
 wxID_FRAME1GENBITMAPTEXTBUTTON10, wxID_FRAME1GENBITMAPTEXTBUTTON11, 
 wxID_FRAME1GENBITMAPTEXTBUTTON2, wxID_FRAME1GENBITMAPTEXTBUTTON3, 
 wxID_FRAME1GENBITMAPTEXTBUTTON4, wxID_FRAME1GENBITMAPTEXTBUTTON5, 
 wxID_FRAME1GENBITMAPTEXTBUTTON6, wxID_FRAME1GENBITMAPTEXTBUTTON7, 
 wxID_FRAME1GENBITMAPTEXTBUTTON8, wxID_FRAME1GENBITMAPTEXTBUTTON9, 
 wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, 
 wxID_FRAME1STATICBOX3, wxID_FRAME1STATICBOX4, 
] = [wx.NewId() for _init_ctrls in range(17)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(493, 263), size=wx.Size(469, 368),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Edit Administrasi Persuratan')
        self.SetClientSize(wx.Size(469, 368))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap('png/sideka.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(24, 0),
              size=wx.Size(288, 65), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Edit Persuratan', name='staticBox1', parent=self,
              pos=wx.Point(24, 64), size=wx.Size(200, 100), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Administrasi Kependudukan', name='staticBox2',
              parent=self, pos=wx.Point(24, 168), size=wx.Size(200, 152),
              style=0)

        self.genBitmapTextButton1 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON1, label=u'Edit Surat Masuk',
              name='genBitmapTextButton1', parent=self, pos=wx.Point(40, 88),
              size=wx.Size(168, 31), style=0)

        self.genBitmapTextButton2 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON2, label=u'Edit Pengantar KTP',
              name='genBitmapTextButton2', parent=self, pos=wx.Point(40, 192),
              size=wx.Size(168, 31), style=0)

        self.genBitmapTextButton3 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON3, label=u'Edit  Pengantar SKCK',
              name='genBitmapTextButton3', parent=self, pos=wx.Point(40, 232),
              size=wx.Size(168, 31), style=0)

        self.genBitmapTextButton4 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON4, label=u'Edit Surat Lainnya',
              name='genBitmapTextButton4', parent=self, pos=wx.Point(40, 272),
              size=wx.Size(168, 31), style=0)

        self.staticBox3 = wx.StaticBox(id=wxID_FRAME1STATICBOX3,
              label=u'Layanan Umum', name='staticBox3', parent=self,
              pos=wx.Point(232, 64), size=wx.Size(216, 152), style=0)

        self.genBitmapTextButton5 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON5,
              label=u'Edit Ktr. Tidak Mampu', name='genBitmapTextButton5',
              parent=self, pos=wx.Point(248, 88), size=wx.Size(184, 31),
              style=0)

        self.genBitmapTextButton6 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON6,
              label=u'Edit Keterangan Domisili', name='genBitmapTextButton6',
              parent=self, pos=wx.Point(248, 128), size=wx.Size(184, 31),
              style=0)

        self.genBitmapTextButton7 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON7,
              label=u'Edit Keterangan Lainnya', name='genBitmapTextButton7',
              parent=self, pos=wx.Point(248, 160), size=wx.Size(184, 31),
              style=0)

        self.staticBox4 = wx.StaticBox(id=wxID_FRAME1STATICBOX4,
              label=u'Perijinan', name='staticBox4', parent=self,
              pos=wx.Point(232, 216), size=wx.Size(216, 104), style=0)

        self.genBitmapTextButton8 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON8,
              label=u'Edit Ijin Menebang Pohon', name='genBitmapTextButton8',
              parent=self, pos=wx.Point(248, 240), size=wx.Size(184, 31),
              style=0)

        self.genBitmapTextButton9 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON9, label=u'Edit Ijin Lainnya',
              name='genBitmapTextButton9', parent=self, pos=wx.Point(248, 280),
              size=wx.Size(184, 31), style=0)

        self.genBitmapTextButton10 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON10, label=u'Edit Surat Keluar',
              name='genBitmapTextButton10', parent=self, pos=wx.Point(40, 128),
              size=wx.Size(168, 31), style=0)

        self.genBitmapTextButton11 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON11,
              label=u'Kembali Ke Menu Utama', name='genBitmapTextButton11',
              parent=self, pos=wx.Point(152, 328), size=wx.Size(184, 31),
              style=0)
        self.genBitmapTextButton11.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton11Button,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON11)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGenBitmapTextButton11Button(self, event):
        event.Skip()
