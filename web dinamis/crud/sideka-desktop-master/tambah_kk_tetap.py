import wx
import wx.lib.buttons

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1CHOICE1, wxID_FRAME1CHOICE10, wxID_FRAME1CHOICE11, 
 wxID_FRAME1CHOICE12, wxID_FRAME1CHOICE13, wxID_FRAME1CHOICE14, 
 wxID_FRAME1CHOICE2, wxID_FRAME1CHOICE3, wxID_FRAME1CHOICE4, 
 wxID_FRAME1CHOICE5, wxID_FRAME1CHOICE6, wxID_FRAME1CHOICE7, 
 wxID_FRAME1CHOICE8, wxID_FRAME1CHOICE9, wxID_FRAME1GENBITMAPTEXTBUTTON1, 
 wxID_FRAME1GENBITMAPTEXTBUTTON2, wxID_FRAME1GENBITMAPTEXTBUTTON3, 
 wxID_FRAME1GENBITMAPTEXTBUTTON4, wxID_FRAME1STATICBITMAP1, 
 wxID_FRAME1STATICBITMAP2, wxID_FRAME1STATICBOX2, wxID_FRAME1STATICBOX3, 
 wxID_FRAME1STATICBOX4, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, 
 wxID_FRAME1STATICTEXT11, wxID_FRAME1STATICTEXT12, wxID_FRAME1STATICTEXT13, 
 wxID_FRAME1STATICTEXT14, wxID_FRAME1STATICTEXT15, wxID_FRAME1STATICTEXT16, 
 wxID_FRAME1STATICTEXT17, wxID_FRAME1STATICTEXT18, wxID_FRAME1STATICTEXT19, 
 wxID_FRAME1STATICTEXT20, wxID_FRAME1STATICTEXT21, wxID_FRAME1STATICTEXT22, 
 wxID_FRAME1STATICTEXT23, wxID_FRAME1STATICTEXT24, wxID_FRAME1STATICTEXT25, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, 
 wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT9, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TEXTCTRL10, wxID_FRAME1TEXTCTRL4, wxID_FRAME1TEXTCTRL5, 
 wxID_FRAME1TEXTCTRL6, wxID_FRAME1TEXTCTRL7, wxID_FRAME1TEXTCTRL8, 
 wxID_FRAME1TEXTCTRL9, 
] = [wx.NewId() for _init_ctrls in range(54)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(341, 152), size=wx.Size(911, 551),
              style=wx.FRAME_NO_TASKBAR,
              title=u'Penambahan Data Keluarga Pada KK Tetap')
        self.SetClientSize(wx.Size(911, 551))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap('png/sideka.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(12, 4),
              size=wx.Size(276, 65), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Nomor KK', name='staticText1', parent=self,
              pos=wx.Point(24, 88), size=wx.Size(65, 17), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(24, 104), size=wx.Size(140, 25),
              style=0, value=u'')

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Data Penduduk', name='staticBox2', parent=self,
              pos=wx.Point(8, 64), size=wx.Size(888, 328), style=0)

        self.staticBitmap2 = wx.StaticBitmap(bitmap=wx.Bitmap('png/photo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP2,
              name='staticBitmap2', parent=self, pos=wx.Point(24, 144),
              size=wx.Size(110, 140), style=0)

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self, pos=wx.Point(176, 104), size=wx.Size(200, 25),
              style=0, value=u'')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'N I K *', name='staticText4', parent=self,
              pos=wx.Point(176, 88), size=wx.Size(40, 17), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Nama Lengkap', name='staticText5', parent=self,
              pos=wx.Point(176, 136), size=wx.Size(98, 17), style=0)

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL5, name='textCtrl5',
              parent=self, pos=wx.Point(176, 152), size=wx.Size(200, 25),
              style=0, value=u'')

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'Jenis Kelamin', name='staticText6', parent=self,
              pos=wx.Point(176, 184), size=wx.Size(84, 17), style=0)

        self.textCtrl6 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL6, name='textCtrl6',
              parent=self, pos=wx.Point(176, 248), size=wx.Size(200, 25),
              style=0, value=u'')

        self.choice1 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE1,
              name='choice1', parent=self, pos=wx.Point(176, 200),
              size=wx.Size(200, 27), style=0)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'Tempat Lahir', name='staticText7', parent=self,
              pos=wx.Point(176, 232), size=wx.Size(83, 17), style=0)

        self.staticBox3 = wx.StaticBox(id=wxID_FRAME1STATICBOX3,
              label=u'Catatan', name='staticBox3', parent=self,
              pos=wx.Point(296, 0), size=wx.Size(600, 65), style=0)

        self.genBitmapTextButton1 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON1,
              label=u'Kembali Ke Menu Utama', name='genBitmapTextButton1',
              parent=self, pos=wx.Point(640, 24), size=wx.Size(240, 31),
              style=0)
        self.genBitmapTextButton1.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton1Button,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON1)

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'Tanggal Lahir', name='staticText9', parent=self,
              pos=wx.Point(176, 280), size=wx.Size(79, 17), style=0)

        self.textCtrl7 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL7, name='textCtrl7',
              parent=self, pos=wx.Point(176, 296), size=wx.Size(200, 25),
              style=0, value=u'')

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'Golongan Darah', name='staticText10', parent=self,
              pos=wx.Point(176, 328), size=wx.Size(98, 17), style=0)

        self.choice2 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE2,
              name='choice2', parent=self, pos=wx.Point(176, 344),
              size=wx.Size(80, 25), style=0)

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label=u'Agama', name='staticText11', parent=self,
              pos=wx.Point(400, 88), size=wx.Size(42, 17), style=0)

        self.choice3 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE3,
              name='choice3', parent=self, pos=wx.Point(400, 104),
              size=wx.Size(216, 25), style=0)

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label=u'Kewarganegaraan', name='staticText12', parent=self,
              pos=wx.Point(400, 136), size=wx.Size(108, 17), style=0)

        self.choice4 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE4,
              name='choice4', parent=self, pos=wx.Point(400, 152),
              size=wx.Size(216, 25), style=0)

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label=u'Pendidikan Terakhir', name='staticText13', parent=self,
              pos=wx.Point(400, 184), size=wx.Size(119, 17), style=0)

        self.choice5 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE5,
              name='choice5', parent=self, pos=wx.Point(400, 200),
              size=wx.Size(216, 25), style=0)

        self.staticText14 = wx.StaticText(id=wxID_FRAME1STATICTEXT14,
              label=u'Pendidikan Yang Saat Ini Ditempuh', name='staticText14',
              parent=self, pos=wx.Point(400, 232), size=wx.Size(210, 17),
              style=0)

        self.choice6 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE6,
              name='choice6', parent=self, pos=wx.Point(400, 248),
              size=wx.Size(216, 25), style=0)

        self.staticText15 = wx.StaticText(id=wxID_FRAME1STATICTEXT15,
              label=u'Pekerjaan Utama', name='staticText15', parent=self,
              pos=wx.Point(400, 280), size=wx.Size(103, 17), style=0)

        self.choice7 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE7,
              name='choice7', parent=self, pos=wx.Point(400, 296),
              size=wx.Size(216, 25), style=0)

        self.staticText16 = wx.StaticText(id=wxID_FRAME1STATICTEXT16,
              label=u'Pekerjaan Lainnya', name='staticText16', parent=self,
              pos=wx.Point(400, 328), size=wx.Size(110, 17), style=0)

        self.textCtrl8 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL8, name='textCtrl8',
              parent=self, pos=wx.Point(400, 344), size=wx.Size(216, 25),
              style=0, value=u'')

        self.staticText17 = wx.StaticText(id=wxID_FRAME1STATICTEXT17,
              label=u'Status Perkawinan', name='staticText17', parent=self,
              pos=wx.Point(632, 88), size=wx.Size(112, 17), style=0)

        self.choice8 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE8,
              name='choice8', parent=self, pos=wx.Point(632, 104),
              size=wx.Size(248, 25), style=0)

        self.staticText18 = wx.StaticText(id=wxID_FRAME1STATICTEXT18,
              label=u'Status Kependudukan', name='staticText18', parent=self,
              pos=wx.Point(632, 136), size=wx.Size(134, 17), style=0)

        self.choice9 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE9,
              name='choice9', parent=self, pos=wx.Point(632, 152),
              size=wx.Size(248, 25), style=0)

        self.staticBox4 = wx.StaticBox(id=wxID_FRAME1STATICBOX4,
              label=u'Hubungan Dengan Keluarga', name='staticBox4', parent=self,
              pos=wx.Point(8, 392), size=wx.Size(888, 100), style=0)

        self.genBitmapTextButton2 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON2,
              label=u'Simpaan & Tambah Data', name='genBitmapTextButton2',
              parent=self, pos=wx.Point(184, 504), size=wx.Size(184, 31),
              style=0)

        self.genBitmapTextButton3 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON3,
              label=u'Simpan & Ke Menu Utama', name='genBitmapTextButton3',
              parent=self, pos=wx.Point(376, 504), size=wx.Size(192, 31),
              style=0)

        self.genBitmapTextButton4 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_FRAME1GENBITMAPTEXTBUTTON4, label=u'Batal Simpan',
              name='genBitmapTextButton4', parent=self, pos=wx.Point(576, 504),
              size=wx.Size(136, 31), style=0)

        self.staticText19 = wx.StaticText(id=wxID_FRAME1STATICTEXT19,
              label=u'Status Tinggal', name='staticText19', parent=self,
              pos=wx.Point(632, 184), size=wx.Size(84, 17), style=0)

        self.choice10 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE10,
              name='choice10', parent=self, pos=wx.Point(632, 200),
              size=wx.Size(248, 25), style=0)

        self.staticText20 = wx.StaticText(id=wxID_FRAME1STATICTEXT20,
              label=u'Penyandang Difabelitas', name='staticText20', parent=self,
              pos=wx.Point(632, 232), size=wx.Size(141, 17), style=0)

        self.choice11 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE11,
              name='choice11', parent=self, pos=wx.Point(632, 248),
              size=wx.Size(248, 25), style=0)

        self.staticText21 = wx.StaticText(id=wxID_FRAME1STATICTEXT21,
              label=u'Penggunaan Kontrasepsi', name='staticText21', parent=self,
              pos=wx.Point(632, 280), size=wx.Size(150, 17), style=0)

        self.choice12 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE12,
              name='choice12', parent=self, pos=wx.Point(632, 296),
              size=wx.Size(248, 25), style=0)

        self.staticText22 = wx.StaticText(id=wxID_FRAME1STATICTEXT22,
              label=u'Kepemilikan Dokumen', name='staticText22', parent=self,
              pos=wx.Point(632, 328), size=wx.Size(136, 17), style=0)

        self.choice13 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE13,
              name='choice13', parent=self, pos=wx.Point(632, 344),
              size=wx.Size(248, 25), style=0)

        self.staticText23 = wx.StaticText(id=wxID_FRAME1STATICTEXT23,
              label=u'Status Hubungan Dalam Keluarga', name='staticText23',
              parent=self, pos=wx.Point(32, 416), size=wx.Size(201, 17),
              style=0)

        self.choice14 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE14,
              name='choice14', parent=self, pos=wx.Point(32, 432),
              size=wx.Size(304, 25), style=0)

        self.staticText24 = wx.StaticText(id=wxID_FRAME1STATICTEXT24,
              label=u'Nama Ayah', name='staticText24', parent=self,
              pos=wx.Point(344, 416), size=wx.Size(70, 17), style=0)

        self.textCtrl9 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL9, name='textCtrl9',
              parent=self, pos=wx.Point(344, 432), size=wx.Size(280, 25),
              style=0, value=u'')

        self.staticText25 = wx.StaticText(id=wxID_FRAME1STATICTEXT25,
              label=u'Nama Ibu', name='staticText25', parent=self,
              pos=wx.Point(632, 416), size=wx.Size(61, 17), style=0)

        self.textCtrl10 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL10,
              name='textCtrl10', parent=self, pos=wx.Point(632, 432),
              size=wx.Size(240, 25), style=0, value=u'')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGenBitmapTextButton1Button(self, event):
        self.main=data_penduduk.create(None)
        self.main.Show()
        self.Close()

    def __init__(self, parent):
        self._init_ctrls(parent)



    def __init__(self, parent):
        self._init_ctrls(parent)
