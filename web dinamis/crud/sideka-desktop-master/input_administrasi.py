import wx
import wx.lib.buttons
import frm_sideka_menu

def create(parent):
    return adm_surat(parent)

[wxID_ADM_SURAT, wxID_ADM_SURATKOTAK_ADM_PENDUDUK, 
 wxID_ADM_SURATKOTAK_LAYANAN_UMUM, wxID_ADM_SURATKOTAK_PERIJINAN, 
 wxID_ADM_SURATKOTAK_PERTANAHAN, wxID_ADM_SURATKOTAK_SURAT_MASUK, 
 wxID_ADM_SURATLOGO, wxID_ADM_SURATTOMBOL_BLOK, wxID_ADM_SURATTOMBOL_DOMISI, 
 wxID_ADM_SURATTOMBOL_IJIN_LAINNYA, wxID_ADM_SURATTOMBOL_IJIN_TEBANG, 
 wxID_ADM_SURATTOMBOL_INPUT_SURAT, wxID_ADM_SURATTOMBOL_KEMBALI_KE_MENU, 
 wxID_ADM_SURATTOMBOL_PERSIL, wxID_ADM_SURATTOMBOL_SURAT_KELUAR, 
 wxID_ADM_SURATTOMBOL_SURAT_KTP, wxID_ADM_SURATTOMBOL_SURAT_PENDUDUK_LAINNYA, 
 wxID_ADM_SURATTOMBOL_SURAT_SKCK, wxID_ADM_SURATTOMBOL_TIDAK_MAMPU, 
 wxID_ADM_SURATTOMBOL_UMUM_LAINNYA, 
] = [wx.NewId() for _init_ctrls in range(20)]

class adm_surat(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_ADM_SURAT, name=u'adm_surat',
              parent=prnt, pos=wx.Point(493, 193), size=wx.Size(488, 445),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Administrasi Persuratan')
        self.SetClientSize(wx.Size(488, 445))

        self.logo = wx.StaticBitmap(bitmap=wx.Bitmap('png/sideka.png',
              wx.BITMAP_TYPE_PNG), id=wxID_ADM_SURATLOGO, name=u'logo',
              parent=self, pos=wx.Point(24, 0), size=wx.Size(288, 65), style=0)

        self.kotak_surat_masuk = wx.StaticBox(id=wxID_ADM_SURATKOTAK_SURAT_MASUK,
              label=u'Surat Masuk', name=u'kotak_surat_masuk', parent=self,
              pos=wx.Point(24, 64), size=wx.Size(200, 100), style=0)

        self.kotak_adm_penduduk = wx.StaticBox(id=wxID_ADM_SURATKOTAK_ADM_PENDUDUK,
              label=u'Administrasi Kependudukan', name=u'kotak_adm_penduduk',
              parent=self, pos=wx.Point(24, 168), size=wx.Size(200, 152),
              style=0)

        self.tombol_input_surat = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADM_SURATTOMBOL_INPUT_SURAT, label=u'Input Surat Masuk',
              name=u'tombol_input_surat', parent=self, pos=wx.Point(40, 88),
              size=wx.Size(168, 31), style=0)

        self.tombol_surat_ktp = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADM_SURATTOMBOL_SURAT_KTP, label=u'Surat Pengantar KTP',
              name=u'tombol_surat_ktp', parent=self, pos=wx.Point(40, 192),
              size=wx.Size(168, 31), style=0)

        self.tombol_surat_skck = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADM_SURATTOMBOL_SURAT_SKCK, label=u'Surat Pengantar SKCK',
              name=u'tombol_surat_skck', parent=self, pos=wx.Point(40, 232),
              size=wx.Size(168, 31), style=0)

        self.tombol_surat_penduduk_lainnya = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADM_SURATTOMBOL_SURAT_PENDUDUK_LAINNYA,
              label=u'Surat Lainnya', name=u'tombol_surat_penduduk_lainnya',
              parent=self, pos=wx.Point(40, 272), size=wx.Size(168, 31),
              style=0)

        self.kotak_layanan_umum = wx.StaticBox(id=wxID_ADM_SURATKOTAK_LAYANAN_UMUM,
              label=u'Layanan Umum', name=u'kotak_layanan_umum', parent=self,
              pos=wx.Point(232, 64), size=wx.Size(216, 152), style=0)

        self.tombol_tidak_mampu = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADM_SURATTOMBOL_TIDAK_MAMPU,
              label=u'Keterangan Tidak Mampu', name=u'tombol_tidak_mampu',
              parent=self, pos=wx.Point(248, 88), size=wx.Size(184, 31),
              style=0)

        self.tombol_domisi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADM_SURATTOMBOL_DOMISI, label=u'Keterangan Domisili',
              name=u'tombol_domisi', parent=self, pos=wx.Point(248, 128),
              size=wx.Size(184, 31), style=0)

        self.tombol_umum_lainnya = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADM_SURATTOMBOL_UMUM_LAINNYA, label=u'Keterangan Lainnya',
              name=u'tombol_umum_lainnya', parent=self, pos=wx.Point(248, 168),
              size=wx.Size(184, 31), style=0)

        self.kotak_perijinan = wx.StaticBox(id=wxID_ADM_SURATKOTAK_PERIJINAN,
              label=u'Perijinan', name=u'kotak_perijinan', parent=self,
              pos=wx.Point(232, 216), size=wx.Size(216, 104), style=0)

        self.tombol_ijin_tebang = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADM_SURATTOMBOL_IJIN_TEBANG, label=u'Ijin Menebang Pohon',
              name=u'tombol_ijin_tebang', parent=self, pos=wx.Point(248, 240),
              size=wx.Size(184, 31), style=0)

        self.tombol_ijin_lainnya = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADM_SURATTOMBOL_IJIN_LAINNYA, label=u'Ijin Lainnya',
              name=u'tombol_ijin_lainnya', parent=self, pos=wx.Point(248, 280),
              size=wx.Size(184, 31), style=0)

        self.tombol_surat_keluar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADM_SURATTOMBOL_SURAT_KELUAR, label=u'Input Surat Keluar',
              name=u'tombol_surat_keluar', parent=self, pos=wx.Point(40, 128),
              size=wx.Size(168, 31), style=0)

        self.tombol_kembali_ke_menu = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADM_SURATTOMBOL_KEMBALI_KE_MENU,
              label=u'Kembali Ke Menu Utama', name=u'tombol_kembali_ke_menu',
              parent=self, pos=wx.Point(160, 400), size=wx.Size(184, 31),
              style=0)
        self.tombol_kembali_ke_menu.Bind(wx.EVT_BUTTON,
              self.OnTombol_kembali_ke_menuButton,
              id=wxID_ADM_SURATTOMBOL_KEMBALI_KE_MENU)

        self.kotak_pertanahan = wx.StaticBox(id=wxID_ADM_SURATKOTAK_PERTANAHAN,
              label=u'Pertanahan', name=u'kotak_pertanahan', parent=self,
              pos=wx.Point(24, 320), size=wx.Size(424, 70), style=0)

        self.tombol_blok = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADM_SURATTOMBOL_BLOK, label=u'Blok', name=u'tombol_blok',
              parent=self, pos=wx.Point(40, 344), size=wx.Size(192, 31),
              style=0)

        self.tombol_persil = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ADM_SURATTOMBOL_PERSIL, label=u'Persil',
              name=u'tombol_persil', parent=self, pos=wx.Point(248, 344),
              size=wx.Size(176, 31), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

        
    def OnTombol_kembali_ke_menuButton(self, event):
        self.Close()
        self.main=frm_sideka_menu.create(None)
        self.main.Show()
