import wx
import input_profil
import peringatan
import frm_sideka_menu


def create(parent):
    return dialog_otentifikasi(parent)

[wxID_DIALOG_OTENTIFIKASI, wxID_DIALOG_OTENTIFIKASIGARIS_ATAS, 
 wxID_DIALOG_OTENTIFIKASIINPUT_PASSWORD, wxID_DIALOG_OTENTIFIKASILABEL_ATAS, 
 wxID_DIALOG_OTENTIFIKASILABEL_PASSWORD, 
 wxID_DIALOG_OTENTIFIKASITOMBOL_KEMBALI_KE_MENU, 
 wxID_DIALOG_OTENTIFIKASITOMBOL_LANJUTKAN, 
] = [wx.NewId() for _init_ctrls in range(7)]

class dialog_otentifikasi(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG_OTENTIFIKASI,
              name=u'dialog_otentifikasi', parent=prnt, pos=wx.Point(515, 304),
              size=wx.Size(402, 140), style=wx.CAPTION, title=u'Otentifikasi')
        self.SetClientSize(wx.Size(402, 140))

        self.label_password = wx.StaticText(id=wxID_DIALOG_OTENTIFIKASILABEL_PASSWORD,
              label=u'Password', name=u'label_password', parent=self,
              pos=wx.Point(16, 64), size=wx.Size(60, 17), style=0)

        self.input_password = wx.TextCtrl(id=wxID_DIALOG_OTENTIFIKASIINPUT_PASSWORD,
              name=u'input_password', parent=self, pos=wx.Point(96, 56),
              size=wx.Size(296, 25), style=wx.TE_PASSWORD, value='')

        self.label_atas = wx.StaticText(id=wxID_DIALOG_OTENTIFIKASILABEL_ATAS,
              label=u'MASUKAN PASSWORD DAHULU', name=u'label_atas', parent=self,
              pos=wx.Point(104, 16), size=wx.Size(203, 17), style=0)

        self.tombol_lanjutkan = wx.Button(id=wxID_DIALOG_OTENTIFIKASITOMBOL_LANJUTKAN,
              label=u'Lanjutkan', name=u'tombol_lanjutkan', parent=self,
              pos=wx.Point(208, 96), size=wx.Size(184, 30), style=0)
        self.tombol_lanjutkan.Bind(wx.EVT_BUTTON, self.OnTombol_lanjutkanButton,
              id=wxID_DIALOG_OTENTIFIKASITOMBOL_LANJUTKAN)

        self.tombol_kembali_ke_menu = wx.Button(id=wxID_DIALOG_OTENTIFIKASITOMBOL_KEMBALI_KE_MENU,
              label=u'Kembali Ke Menu', name=u'tombol_kembali_ke_menu',
              parent=self, pos=wx.Point(16, 96), size=wx.Size(184, 30),
              style=0)
        self.tombol_kembali_ke_menu.Bind(wx.EVT_BUTTON,
              self.OnTombol_kembali_ke_menuButton,
              id=wxID_DIALOG_OTENTIFIKASITOMBOL_KEMBALI_KE_MENU)

        self.garis_atas = wx.StaticLine(id=wxID_DIALOG_OTENTIFIKASIGARIS_ATAS,
              name=u'garis_atas', parent=self, pos=wx.Point(16, 40),
              size=wx.Size(368, 2), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTombol_lanjutkanButton(self, event):
        oneng = 'andri'
        user_password = self.input_password.GetValue()
        if user_password == oneng:
            
            self.main=input_profil.create(None)
            self.main.Show()
            self.Close()
         
       
        else:
            self.Close()
            self.main=peringatan.create(None)
            self.main.Show()

    def OnTombol_kembali_ke_menuButton(self, event):
        self.Close()
        self.main=frm_sideka_menu.create(None)
        self.main.Show()

     
       
       
