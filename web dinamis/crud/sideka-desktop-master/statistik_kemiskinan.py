import wx
import wx.lib.buttons

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GENBITMAPTEXTBUTTON1, 
 wxID_FRAME1GENBITMAPTEXTBUTTON2, wxID_FRAME1GENBITMAPTEXTBUTTON3, 
 wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICBOX1, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(530, 312), size=wx.Size(306, 235),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Data Statistik Kemiskinan')
        self.SetClientSize(wx.Size(306, 235))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap('png/sideka.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(288, 72), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Statistik Kemiskinan', name='staticBox1', parent=self,
              pos=wx.Point(16, 72), size=wx.Size(272, 105), style=0)

        self.genBitmapTextButton1 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON1, label=u'Data Miskin Desa',
              name='genBitmapTextButton1', parent=self, pos=wx.Point(32, 96),
              size=wx.Size(240, 31), style=0)

        self.genBitmapTextButton2 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON2,
              label=u'Perbandingan Prog. Perlindungan',
              name='genBitmapTextButton2', parent=self, pos=wx.Point(32, 136),
              size=wx.Size(240, 31), style=0)

        self.genBitmapTextButton3 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON3,
              label=u'Kembali Ke Menu Utama', name='genBitmapTextButton3',
              parent=self, pos=wx.Point(32, 184), size=wx.Size(240, 31),
              style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
