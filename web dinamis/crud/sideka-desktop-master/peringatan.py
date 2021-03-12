import wx
import frm_sideka_menu

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(557, 314), size=wx.Size(221, 97),
              style=wx.CAPTION, title=u'Peringatan !!!')
        self.SetClientSize(wx.Size(221, 97))

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label=u'Anda Tidak Berhak\nMelakukan Perubahan\nDan Penambahan Data !!!',
              name='staticText1', parent=self, pos=wx.Point(24, 8),
              size=wx.Size(170, 51), style=0)

        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1,
              label=u'Kembali Ke Menu Utama', name='button1', parent=self,
              pos=wx.Point(8, 64), size=wx.Size(200, 30), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG1BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.main=frm_sideka_menu.create(None)
        self.main.Show()
        self.Close()
        event.Skip()
