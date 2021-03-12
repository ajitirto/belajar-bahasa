import wx
import input_administrasi_surat
import peringatan
import frm_sideka_menu


def create(parent):
    return dialog_login_surat(parent)

[wxID_DIALOG_LOGIN_SURAT, wxID_DIALOG_LOGIN_SURATBUTTON2, 
 wxID_DIALOG_LOGIN_SURATSTATICLINE1, wxID_DIALOG_LOGIN_SURATSTATICTEXT1, 
 wxID_DIALOG_LOGIN_SURATSTATICTEXT2, wxID_DIALOG_LOGIN_SURATTEXTCTRL1, 
 wxID_DIALOG_LOGIN_SURATTOMBOL_LANJUTKAN, 
] = [wx.NewId() for _init_ctrls in range(7)]

class dialog_login_surat(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG_LOGIN_SURAT,
              name=u'dialog_login_surat', parent=prnt, pos=wx.Point(515, 304),
              size=wx.Size(402, 140), style=wx.CAPTION, title=u'Otentifikasi')
        self.SetClientSize(wx.Size(402, 140))

        self.staticText1 = wx.StaticText(id=wxID_DIALOG_LOGIN_SURATSTATICTEXT1,
              label=u'Password', name='staticText1', parent=self,
              pos=wx.Point(16, 64), size=wx.Size(60, 17), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_DIALOG_LOGIN_SURATTEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(96, 56),
              size=wx.Size(296, 25), style=wx.TE_PASSWORD, value='')

        self.staticText2 = wx.StaticText(id=wxID_DIALOG_LOGIN_SURATSTATICTEXT2,
              label=u'MASUKAN PASSWORD DAHULU', name='staticText2', parent=self,
              pos=wx.Point(104, 16), size=wx.Size(203, 17), style=0)

        self.tombol_lanjutkan = wx.Button(id=wxID_DIALOG_LOGIN_SURATTOMBOL_LANJUTKAN,
              label=u'Lanjutkan', name=u'tombol_lanjutkan', parent=self,
              pos=wx.Point(208, 96), size=wx.Size(184, 30), style=0)
        self.tombol_lanjutkan.Bind(wx.EVT_BUTTON, self.OnTombol_lanjutkanButton,
              id=wxID_DIALOG_LOGIN_SURATTOMBOL_LANJUTKAN)

        self.button2 = wx.Button(id=wxID_DIALOG_LOGIN_SURATBUTTON2,
              label=u'Kembali Ke Menu', name='button2', parent=self,
              pos=wx.Point(16, 96), size=wx.Size(184, 30), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_DIALOG_LOGIN_SURATBUTTON2)

        self.staticLine1 = wx.StaticLine(id=wxID_DIALOG_LOGIN_SURATSTATICLINE1,
              name='staticLine1', parent=self, pos=wx.Point(16, 40),
              size=wx.Size(368, 2), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton2Button(self, event):
        self.Close()
        self.main=frm_sideka_menu.create(None)
        self.main.Show()

    def OnTombol_lanjutkanButton(self, event):
        oneng = 'andri'
        user_password = self.textCtrl1.GetValue()
        if user_password == oneng:
            
            self.main=input_administrasi_surat.create(None)
            self.main.Show()
            self.Close()
         
       
        else:
            self.Close()
            self.main=peringatan.create(None)
            self.main.Show()
