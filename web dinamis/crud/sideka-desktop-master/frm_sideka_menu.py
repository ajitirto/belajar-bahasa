import wx
import bantuan 
import login_input_penduduk
import login_edit_kemiskinan
import login_edit_penduduk
import login_edit_profil
import login_edit_surat
import login_ekonomi
import login_indikator_kemiskinan
import login_input_kemiskinan
import login_input_profil
import login_input_surat
import login_inventaris_desa
import login_lahan
import login_pariwisata
import login_pecah_keluarga
import login_tambak
import cari_penduduk
import laporan_penduduk
import cari_kemiskinan
import laporan_kemiskinan
import wx.lib.buttons
import cari_administrasi
import laporan_administrasi
import laporan_potensi
import laporan_profil
import laporan_statistik
import statistik_penduduk
import statistik_kemiskinan
import statistik_potensi
import statistik_administrasi

def create(parent):
    return sideka(parent)

[wxID_SIDEKA, wxID_SIDEKAGAMBAR_LOGO, wxID_SIDEKAGARIS_ATAS, 
 wxID_SIDEKAGARIS_PROFIL, wxID_SIDEKAKOTAK_ADMINISTRASI, 
 wxID_SIDEKAKOTAK_KEMISKINAN, wxID_SIDEKAKOTAK_MENU_UTAMA, 
 wxID_SIDEKAKOTAK_POTENSI, wxID_SIDEKAKOTAK_STATISTIK, 
 wxID_SIDEKAKOTA_PENDUDUK, wxID_SIDEKALABEL_PRAKARSA, wxID_SIDEKALABEL_PROFIL, 
 wxID_SIDEKALABEL_SIDEKA_ONLINE, wxID_SIDEKATOMBOL_BANTUAN, 
 wxID_SIDEKATOMBOL_CARI_ADMINISTRASI, wxID_SIDEKATOMBOL_CARI_PENDUDUK, 
 wxID_SIDEKATOMBOL_EDIT_DATA_KEMISKINAN, wxID_SIDEKATOMBOL_EDIT_PENDUDUK, 
 wxID_SIDEKATOMBOL_EDIT_PROFIL, wxID_SIDEKATOMBOL_EDIT_SURAT, 
 wxID_SIDEKATOMBOL_EKONOMI, wxID_SIDEKATOMBOL_INPUT_PROFIL, 
 wxID_SIDEKATOMBOL_INVENTARIS_DESA, wxID_SIDEKATOMBOL_KELUAR, 
 wxID_SIDEKATOMBOL_KEPENDUDUKAN, wxID_SIDEKATOMBOL_LAHAN, 
 wxID_SIDEKATOMBOL_LAPORAN_ADMINISTRASI, wxID_SIDEKATOMBOL_LAPORAN_KEMISKINAN, 
 wxID_SIDEKATOMBOL_LAPORAN_PENDUDUK, wxID_SIDEKATOMBOL_LAPORAN_POTENSI, 
 wxID_SIDEKATOMBOL_LAPORAN_PROFIL, wxID_SIDEKATOMBOL_LAPORAN_STATISTIK, 
 wxID_SIDEKATOMBOL_PARIWISATA, wxID_SIDEKATOMBOL_PASSWORD, 
 wxID_SIDEKATOMBOL_PECAH_KELUARGA, wxID_SIDEKATOMBOL_PENCARIAN_KEMISKINAN, 
 wxID_SIDEKATOMBOL_SINKRON, wxID_SIDEKATOMBOL_STATISTIK_ADMINISTRASI, 
 wxID_SIDEKATOMBOL_STATISTIK_KEMISKINAN, wxID_SIDEKATOMBOL_STATISTIK_PENDUDUK, 
 wxID_SIDEKATOMBOL_STATISTIK_POTENSI, wxID_SIDEKATOMBOL_SURAT_MASUK, 
 wxID_SIDEKATOMBOL_TAMBAH_DATA_KEMISKINAN, wxID_SIDEKATOMBOL_TAMBAK, 
 wxID_SIDEKATOMOBOL_INDIKATOR_KEMISKINAN, 
] = [wx.NewId() for _init_ctrls in range(45)]

class sideka(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SIDEKA, name=u'sideka', parent=prnt,
              pos=wx.Point(435, 85), size=wx.Size(647, 616),
              style=wx.FRAME_NO_TASKBAR, title=u'SIDEKA')
        self.SetClientSize(wx.Size(647, 616))

        self.kotak_menu_utama = wx.StaticBox(id=wxID_SIDEKAKOTAK_MENU_UTAMA,
              label=u'MENU UTAMA', name=u'kotak_menu_utama', parent=self,
              pos=wx.Point(16, 88), size=wx.Size(200, 235), style=0)

        self.kota_penduduk = wx.StaticBox(id=wxID_SIDEKAKOTA_PENDUDUK,
              label=u'PENDUDUK', name=u'kota_penduduk', parent=self,
              pos=wx.Point(224, 88), size=wx.Size(200, 235), style=0)

        self.kotak_kemiskinan = wx.StaticBox(id=wxID_SIDEKAKOTAK_KEMISKINAN,
              label=u'KEMISKINAN', name=u'kotak_kemiskinan', parent=self,
              pos=wx.Point(432, 88), size=wx.Size(200, 235), style=0)

        self.kotak_administrasi = wx.StaticBox(id=wxID_SIDEKAKOTAK_ADMINISTRASI,
              label=u'ADMINISTRASI', name=u'kotak_administrasi', parent=self,
              pos=wx.Point(16, 328), size=wx.Size(200, 235), style=0)

        self.kotak_potensi = wx.StaticBox(id=wxID_SIDEKAKOTAK_POTENSI,
              label=u'POTENSI DESA', name=u'kotak_potensi', parent=self,
              pos=wx.Point(224, 328), size=wx.Size(200, 235), style=0)

        self.tombol_kependudukan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/plus14.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_KEPENDUDUKAN,
              label=u'  Kependudukan', name=u'tombol_kependudukan', parent=self,
              pos=wx.Point(240, 112), size=wx.Size(168, 32), style=0)
        self.tombol_kependudukan.Bind(wx.EVT_BUTTON,
              self.OnTombol_kependudukanButton,
              id=wxID_SIDEKATOMBOL_KEPENDUDUKAN)

        self.tombol_pecah_keluarga = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/edit.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_PECAH_KELUARGA,
              label=u'  Pecah Keluarga', name=u'tombol_pecah_keluarga',
              parent=self, pos=wx.Point(240, 152), size=wx.Size(168, 32),
              style=0)
        self.tombol_pecah_keluarga.Bind(wx.EVT_BUTTON,
              self.OnTombol_pecah_keluargaButton,
              id=wxID_SIDEKATOMBOL_PECAH_KELUARGA)

        self.tombol_edit_penduduk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/edit.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_EDIT_PENDUDUK,
              label=u' Edit Penduduk', name=u'tombol_edit_penduduk',
              parent=self, pos=wx.Point(240, 192), size=wx.Size(168, 32),
              style=0)
        self.tombol_edit_penduduk.Bind(wx.EVT_BUTTON,
              self.OnTombol_edit_pendudukButton,
              id=wxID_SIDEKATOMBOL_EDIT_PENDUDUK)

        self.tombol_cari_penduduk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/cari.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_CARI_PENDUDUK,
              label=u'  Cari Penduduk', name=u'tombol_cari_penduduk',
              parent=self, pos=wx.Point(240, 232), size=wx.Size(168, 32),
              style=0)
        self.tombol_cari_penduduk.Bind(wx.EVT_BUTTON,
              self.OnTombol_cari_pendudukButton,
              id=wxID_SIDEKATOMBOL_CARI_PENDUDUK)

        self.tombol_laporan_penduduk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/laporan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_LAPORAN_PENDUDUK,
              label=u' Laporan Penduduk', name=u'tombol_laporan_penduduk',
              parent=self, pos=wx.Point(240, 272), size=wx.Size(168, 32),
              style=0)
        self.tombol_laporan_penduduk.Bind(wx.EVT_BUTTON,
              self.OnTombol_laporan_pendudukButton,
              id=wxID_SIDEKATOMBOL_LAPORAN_PENDUDUK)

        self.tombol_tambah_data_kemiskinan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/plus14.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_TAMBAH_DATA_KEMISKINAN,
              label=u'  Tambah Data', name=u'tombol_tambah_data_kemiskinan',
              parent=self, pos=wx.Point(448, 112), size=wx.Size(168, 32),
              style=0)
        self.tombol_tambah_data_kemiskinan.Bind(wx.EVT_BUTTON,
              self.OnTombol_tambah_data_kemiskinanButton,
              id=wxID_SIDEKATOMBOL_TAMBAH_DATA_KEMISKINAN)

        self.tomobol_indikator_kemiskinan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/plus14.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMOBOL_INDIKATOR_KEMISKINAN,
              label=u'  Indikator', name=u'tomobol_indikator_kemiskinan',
              parent=self, pos=wx.Point(448, 152), size=wx.Size(168, 32),
              style=0)
        self.tomobol_indikator_kemiskinan.Bind(wx.EVT_BUTTON,
              self.OnTomobol_indikator_kemiskinanButton,
              id=wxID_SIDEKATOMOBOL_INDIKATOR_KEMISKINAN)

        self.kotak_statistik = wx.StaticBox(id=wxID_SIDEKAKOTAK_STATISTIK,
              label=u'STATISTIK', name=u'kotak_statistik', parent=self,
              pos=wx.Point(432, 328), size=wx.Size(200, 235), style=0)

        self.tombol_input_profil = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/plus14.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_INPUT_PROFIL,
              label=u'  Input Profil', name=u'tombol_input_profil', parent=self,
              pos=wx.Point(32, 192), size=wx.Size(168, 32), style=0)
        self.tombol_input_profil.Bind(wx.EVT_BUTTON,
              self.OnTombol_input_profilButton,
              id=wxID_SIDEKATOMBOL_INPUT_PROFIL)

        self.tombol_edit_profil = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/edit.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_EDIT_PROFIL,
              label=u'  Edit Profil', name=u'tombol_edit_profil', parent=self,
              pos=wx.Point(32, 232), size=wx.Size(168, 32), style=0)
        self.tombol_edit_profil.Bind(wx.EVT_BUTTON,
              self.OnTombol_edit_profilButton,
              id=wxID_SIDEKATOMBOL_EDIT_PROFIL)

        self.tombol_sinkron = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/sinkron.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_SINKRON,
              label=u'Sinkron Data', name=u'tombol_sinkron', parent=self,
              pos=wx.Point(296, 40), size=wx.Size(168, 32), style=0)

        self.tombol_bantuan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/bantuan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_BANTUAN,
              label=u'  Bantuan', name=u'tombol_bantuan', parent=self,
              pos=wx.Point(472, 40), size=wx.Size(168, 32), style=0)
        self.tombol_bantuan.Bind(wx.EVT_BUTTON, self.OnTombol_bantuanButton,
              id=wxID_SIDEKATOMBOL_BANTUAN)

        self.garis_atas = wx.StaticLine(id=wxID_SIDEKAGARIS_ATAS,
              name=u'garis_atas', parent=self, pos=wx.Point(16, 80),
              size=wx.Size(616, 2), style=0)

        self.tombol_edit_data_kemiskinan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/edit.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_EDIT_DATA_KEMISKINAN,
              label=u' Edit Data Kemiskinan',
              name=u'tombol_edit_data_kemiskinan', parent=self,
              pos=wx.Point(448, 192), size=wx.Size(168, 32), style=0)
        self.tombol_edit_data_kemiskinan.Bind(wx.EVT_BUTTON,
              self.OnTombol_edit_data_kemiskinanButton,
              id=wxID_SIDEKATOMBOL_EDIT_DATA_KEMISKINAN)

        self.tombol_pencarian_kemiskinan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/cari.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_PENCARIAN_KEMISKINAN,
              label=u' Pencarian Data', name=u'tombol_pencarian_kemiskinan',
              parent=self, pos=wx.Point(448, 232), size=wx.Size(168, 32),
              style=0)
        self.tombol_pencarian_kemiskinan.Bind(wx.EVT_BUTTON,
              self.OnTombol_pencarian_kemiskinanButton,
              id=wxID_SIDEKATOMBOL_PENCARIAN_KEMISKINAN)

        self.tombol_laporan_kemiskinan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/laporan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_LAPORAN_KEMISKINAN,
              label=u' Laporan Kemiskinan', name=u'tombol_laporan_kemiskinan',
              parent=self, pos=wx.Point(448, 272), size=wx.Size(168, 32),
              style=0)
        self.tombol_laporan_kemiskinan.Bind(wx.EVT_BUTTON,
              self.OnTombol_laporan_kemiskinanButton,
              id=wxID_SIDEKATOMBOL_LAPORAN_KEMISKINAN)

        self.tombol_surat_masuk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/plus14.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_SURAT_MASUK,
              label=u' Surat Masuk/Keluar', name=u'tombol_surat_masuk',
              parent=self, pos=wx.Point(32, 352), size=wx.Size(168, 32),
              style=0)
        self.tombol_surat_masuk.Bind(wx.EVT_BUTTON,
              self.OnTombol_surat_masukButton,
              id=wxID_SIDEKATOMBOL_SURAT_MASUK)

        self.tombol_edit_surat = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/edit.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_EDIT_SURAT,
              label=u' Edit Data Surat', name=u'tombol_edit_surat', parent=self,
              pos=wx.Point(32, 392), size=wx.Size(168, 32), style=0)
        self.tombol_edit_surat.Bind(wx.EVT_BUTTON,
              self.OnTombol_edit_suratButton, id=wxID_SIDEKATOMBOL_EDIT_SURAT)

        self.tombol_inventaris_desa = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/plus14.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_INVENTARIS_DESA,
              label=u' Inventaris Desa', name=u'tombol_inventaris_desa',
              parent=self, pos=wx.Point(32, 432), size=wx.Size(168, 32),
              style=0)
        self.tombol_inventaris_desa.Bind(wx.EVT_BUTTON,
              self.OnTombol_inventaris_desaButton,
              id=wxID_SIDEKATOMBOL_INVENTARIS_DESA)

        self.tombol_cari_administrasi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/cari.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_CARI_ADMINISTRASI,
              label=u' Pencarian Data', name=u'tombol_cari_administrasi',
              parent=self, pos=wx.Point(32, 472), size=wx.Size(168, 32),
              style=0)
        self.tombol_cari_administrasi.Bind(wx.EVT_BUTTON,
              self.OnTombol_cari_administrasiButton,
              id=wxID_SIDEKATOMBOL_CARI_ADMINISTRASI)

        self.tombol_laporan_administrasi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/laporan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_LAPORAN_ADMINISTRASI,
              label=u'Laporan Administrasi',
              name=u'tombol_laporan_administrasi', parent=self, pos=wx.Point(32,
              512), size=wx.Size(168, 32), style=0)
        self.tombol_laporan_administrasi.Bind(wx.EVT_BUTTON,
              self.OnTombol_laporan_administrasiButton,
              id=wxID_SIDEKATOMBOL_LAPORAN_ADMINISTRASI)

        self.label_sideka_online = wx.StaticText(id=wxID_SIDEKALABEL_SIDEKA_ONLINE,
              label=u' SIDEKA ONLINE :', name=u'label_sideka_online',
              parent=self, pos=wx.Point(304, 16), size=wx.Size(112, 17),
              style=0)

        self.tombol_password = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/security1.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_PASSWORD,
              label=u'  Password', name=u'tombol_password', parent=self,
              pos=wx.Point(32, 112), size=wx.Size(168, 32), style=0)

        self.label_profil = wx.StaticText(id=wxID_SIDEKALABEL_PROFIL,
              label=u'PROFIL DESA', name=u'label_profil', parent=self,
              pos=wx.Point(72, 168), size=wx.Size(84, 17), style=0)

        self.tombol_laporan_profil = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/laporan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_LAPORAN_PROFIL,
              label=u' Laporan Profil', name=u'tombol_laporan_profil',
              parent=self, pos=wx.Point(32, 272), size=wx.Size(168, 32),
              style=0)
        self.tombol_laporan_profil.Bind(wx.EVT_BUTTON,
              self.OnTombol_laporan_profilButton,
              id=wxID_SIDEKATOMBOL_LAPORAN_PROFIL)

        self.tombol_ekonomi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/bantuan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_EKONOMI,
              label=u' Ekonomi SosBud', name=u'tombol_ekonomi', parent=self,
              pos=wx.Point(240, 352), size=wx.Size(168, 32), style=0)
        self.tombol_ekonomi.Bind(wx.EVT_BUTTON, self.OnTombol_ekonomiButton,
              id=wxID_SIDEKATOMBOL_EKONOMI)

        self.garis_profil = wx.StaticLine(id=wxID_SIDEKAGARIS_PROFIL,
              name=u'garis_profil', parent=self, pos=wx.Point(24, 152),
              size=wx.Size(184, 2), style=0)

        self.label_prakarsa = wx.StaticText(id=wxID_SIDEKALABEL_PRAKARSA,
              label=u'Prakarsa Desa 2015', name=u'label_prakarsa', parent=self,
              pos=wx.Point(504, 592), size=wx.Size(130, 17), style=0)

        self.tombol_keluar = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/delete25.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_KELUAR,
              label=u'  Keluar Dari Program SIDEKA', name=u'tombol_keluar',
              parent=self, pos=wx.Point(208, 576), size=wx.Size(240, 31),
              style=0)
        self.tombol_keluar.Bind(wx.EVT_BUTTON, self.OnTombol_keluarButton,
              id=wxID_SIDEKATOMBOL_KELUAR)

        self.gambar_logo = wx.StaticBitmap(bitmap=wx.Bitmap('png/sideka.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKAGAMBAR_LOGO,
              name=u'gambar_logo', parent=self, pos=wx.Point(16, 8),
              size=wx.Size(272, 64), style=0)

        self.tombol_statistik_penduduk = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/pen.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_STATISTIK_PENDUDUK,
              label=u' Statistik Penduduk', name=u'tombol_statistik_penduduk',
              parent=self, pos=wx.Point(448, 352), size=wx.Size(168, 31),
              style=0)
        self.tombol_statistik_penduduk.Bind(wx.EVT_BUTTON,
              self.OnTombol_statistik_pendudukButton,
              id=wxID_SIDEKATOMBOL_STATISTIK_PENDUDUK)

        self.tombol_statistik_kemiskinan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/statistikmiskin.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_STATISTIK_KEMISKINAN,
              label=u' Statistik Kemiskinan',
              name=u'tombol_statistik_kemiskinan', parent=self,
              pos=wx.Point(448, 392), size=wx.Size(168, 31), style=0)
        self.tombol_statistik_kemiskinan.Bind(wx.EVT_BUTTON,
              self.OnTombol_statistik_kemiskinanButton,
              id=wxID_SIDEKATOMBOL_STATISTIK_KEMISKINAN)

        self.tombol_statistik_potensi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/potensi.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_STATISTIK_POTENSI,
              label=u' Statistik Potensi', name=u'tombol_statistik_potensi',
              parent=self, pos=wx.Point(448, 432), size=wx.Size(168, 31),
              style=0)
        self.tombol_statistik_potensi.Bind(wx.EVT_BUTTON,
              self.OnTombol_statistik_potensiButton,
              id=wxID_SIDEKATOMBOL_STATISTIK_POTENSI)

        self.tombol_statistik_administrasi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/adm2.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_STATISTIK_ADMINISTRASI,
              label=u' Statistik Administrasi',
              name=u'tombol_statistik_administrasi', parent=self,
              pos=wx.Point(448, 472), size=wx.Size(168, 31), style=0)
        self.tombol_statistik_administrasi.Bind(wx.EVT_BUTTON,
              self.OnTombol_statistik_administrasiButton,
              id=wxID_SIDEKATOMBOL_STATISTIK_ADMINISTRASI)

        self.tombol_laporan_statistik = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/laporan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_LAPORAN_STATISTIK,
              label=u'  Laporan', name=u'tombol_laporan_statistik', parent=self,
              pos=wx.Point(448, 512), size=wx.Size(168, 31), style=0)
        self.tombol_laporan_statistik.Bind(wx.EVT_BUTTON,
              self.OnTombol_laporan_statistikButton,
              id=wxID_SIDEKATOMBOL_LAPORAN_STATISTIK)

        self.tombol_lahan = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/lahan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_LAHAN,
              label=u' Lahan & Sumber Air', name=u'tombol_lahan', parent=self,
              pos=wx.Point(240, 392), size=wx.Size(168, 31), style=0)
        self.tombol_lahan.Bind(wx.EVT_BUTTON, self.OnTombol_lahanButton,
              id=wxID_SIDEKATOMBOL_LAHAN)

        self.tombol_tambak = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/tambak.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_TAMBAK,
              label=u' Tambak / Kolam Ikan', name=u'tombol_tambak', parent=self,
              pos=wx.Point(240, 432), size=wx.Size(168, 31), style=0)
        self.tombol_tambak.Bind(wx.EVT_BUTTON, self.OnTombol_tambakButton,
              id=wxID_SIDEKATOMBOL_TAMBAK)

        self.tombol_pariwisata = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/pariwisata.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_PARIWISATA,
              label=u' Pariwisata', name=u'tombol_pariwisata', parent=self,
              pos=wx.Point(240, 472), size=wx.Size(168, 31), style=0)
        self.tombol_pariwisata.Bind(wx.EVT_BUTTON,
              self.OnTombol_pariwisataButton, id=wxID_SIDEKATOMBOL_PARIWISATA)

        self.tombol_laporan_potensi = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.Bitmap('png/laporan.png',
              wx.BITMAP_TYPE_PNG), id=wxID_SIDEKATOMBOL_LAPORAN_POTENSI,
              label=u' Laporan Potensi', name=u'tombol_laporan_potensi',
              parent=self, pos=wx.Point(240, 512), size=wx.Size(168, 31),
              style=0)
        self.tombol_laporan_potensi.Bind(wx.EVT_BUTTON,
              self.OnTombol_laporan_potensiButton,
              id=wxID_SIDEKATOMBOL_LAPORAN_POTENSI)

    def __init__(self, parent):
                self._init_ctrls(parent)
    
    def OnTombol_bantuanButton(self, event):
        self.main=bantuan.create(None)
        self.main.Show()

    def OnTombol_input_profilButton(self, event):
        self.main=login_input_profil.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_edit_profilButton(self, event):
        self.main=login_edit_profil.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_laporan_profilButton(self, event):
        self.main=laporan_profil.create(None)
        self.main.Show()
        self.Close()
   
    def OnTombol_kependudukanButton(self, event):
        self.main=login_input_penduduk.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_pecah_keluargaButton(self, event):
        self.main=login_pecah_keluarga.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_edit_pendudukButton(self, event):
        self.main=login_edit_penduduk.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_cari_pendudukButton(self, event):
        self.main=cari_penduduk.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_laporan_pendudukButton(self, event):
        self.main=laporan_penduduk.create(None)
        self.main.Show()
        self.Close()
    
    def OnTombol_tambah_data_kemiskinanButton(self, event):
        self.main=login_input_kemiskinan.create(None)
        self.main.Show()
        self.Close()

    def OnTomobol_indikator_kemiskinanButton(self, event):
        self.main=login_indikator_kemiskinan.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_edit_data_kemiskinanButton(self, event):
        self.main=login_edit_kemiskinan.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_pencarian_kemiskinanButton(self, event):
        self.main=cari_kemiskinan.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_laporan_kemiskinanButton(self, event):
        self.main=laporan_kemiskinan.create(None)
        self.main.Show()
        self.Close()
   
    def OnTombol_surat_masukButton(self, event):
        self.main=login_input_surat.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_edit_suratButton(self, event):
        self.main=login_edit_surat.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_inventaris_desaButton(self, event):
        self.main=login_inventaris_desa.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_cari_administrasiButton(self, event):
        self.main=cari_administrasi.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_laporan_administrasiButton(self, event):
        self.main=laporan_administrasi.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_ekonomiButton(self, event):
        self.main=login_ekonomi.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_lahanButton(self, event):
        self.main=login_lahan.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_tambakButton(self, event):
        self.main=login_tambak.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_pariwisataButton(self, event):
        self.main=login_pariwisata.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_laporan_potensiButton(self, event):
        self.main=laporan_potensi.create(None)
        self.main.Show()
        self.Close()
        
    def OnTombol_statistik_pendudukButton(self, event):
        self.main=statistik_penduduk.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_statistik_kemiskinanButton(self, event):
        self.main=statistik_kemiskinan.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_statistik_potensiButton(self, event):
        self.main=statistik_potensi.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_statistik_administrasiButton(self, event):
        self.main=statistik_administrasi.create(None)
        self.main.Show()
        self.Close()

    def OnTombol_laporan_statistikButton(self, event):
        self.main=laporan_statistik.create(None)
        self.main.Show()
        self.Close()
    
    def OnTombol_keluarButton(self, event):
        self.Close()  
