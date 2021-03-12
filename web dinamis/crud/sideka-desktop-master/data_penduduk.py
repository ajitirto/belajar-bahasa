import wx
import wx.lib.buttons
import kk_sementara
import frm_sideka_menu
import kk_tetap

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GENBITMAPTEXTBUTTON1, 
 wxID_FRAME1GENBITMAPTEXTBUTTON11, wxID_FRAME1GENBITMAPTEXTBUTTON2, 
 wxID_FRAME1GENBITMAPTEXTBUTTON3, wxID_FRAME1GENBITMAPTEXTBUTTON4, 
 wxID_FRAME1GENBITMAPTEXTBUTTON6, wxID_FRAME1GENBITMAPTEXTBUTTON7, 
 wxID_FRAME1GENBITMAPTEXTBUTTON8, wxID_FRAME1GENBITMAPTEXTBUTTON9, 
 wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, 
] = [wx.NewId() for _init_ctrls in range(13)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(487, 280), size=wx.Size(455, 316),
              style=wx.FRAME_NO_TASKBAR, title=u'Kependudukan')
        self.SetClientSize(wx.Size(455, 316))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap('png/sideka.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(16, 8),
              size=wx.Size(260, 70), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Penambahan', name='staticBox1', parent=self,
              pos=wx.Point(16, 72), size=wx.Size(200, 190), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Peristiwa', name='staticBox2', parent=self,
              pos=wx.Point(232, 72), size=wx.Size(200, 190), style=0)

        self.genBitmapTextButton1 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON1, label=u'Buat KK Sementara',
              name='genBitmapTextButton1', parent=self, pos=wx.Point(24, 96),
              size=wx.Size(184, 31), style=0)
        self.genBitmapTextButton1.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton1Button,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON1)

        self.genBitmapTextButton2 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON2, label=u'Buat KK Tetap',
              name='genBitmapTextButton2', parent=self, pos=wx.Point(24, 136),
              size=wx.Size(184, 31), style=0)
        self.genBitmapTextButton2.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton2Button,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON2)

        self.genBitmapTextButton3 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON3, label=u'Anggota KK Sementara',
              name='genBitmapTextButton3', parent=self, pos=wx.Point(24, 176),
              size=wx.Size(184, 31), style=0)

        self.genBitmapTextButton4 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON4, label=u'Anggota KK Tetap',
              name='genBitmapTextButton4', parent=self, pos=wx.Point(24, 216),
              size=wx.Size(184, 31), style=0)

        self.genBitmapTextButton6 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON6, label=u'Kelahiran',
              name='genBitmapTextButton6', parent=self, pos=wx.Point(240, 96),
              size=wx.Size(184, 31), style=0)

        self.genBitmapTextButton7 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON7, label=u'Kematian',
              name='genBitmapTextButton7', parent=self, pos=wx.Point(240, 136),
              size=wx.Size(184, 31), style=0)

        self.genBitmapTextButton8 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON8, label=u'Pindah',
              name='genBitmapTextButton8', parent=self, pos=wx.Point(240, 176),
              size=wx.Size(184, 31), style=0)

        self.genBitmapTextButton9 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON9, label=u'Peristiwa Lain',
              name='genBitmapTextButton9', parent=self, pos=wx.Point(240, 216),
              size=wx.Size(184, 31), style=0)

        self.genBitmapTextButton11 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON11,
              label=u'Kembali Ke Menu Utama', name='genBitmapTextButton11',
              parent=self, pos=wx.Point(120, 272), size=wx.Size(208, 31),
              style=0)
        self.genBitmapTextButton11.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton11Button,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON11)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGenBitmapTextButton1Button(self, event):
        self.main=kk_sementara.create(None)
        self.main.Show()
        self.Close()

    def OnGenBitmapTextButton11Button(self, event):
        self.main=frm_sideka_menu.create(None)
        self.main.Show()
        self.Close()

    def OnGenBitmapTextButton2Button(self, event):
        self.main=kk_tetap.create(None)
        self.main.Show()
        self.Close()

