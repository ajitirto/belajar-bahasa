import wx

def create(parent):
    return frm_cari_adm(parent)

[wxID_FRM_CARI_ADM] = [wx.NewId() for _init_ctrls in range(1)]

class frm_cari_adm(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRM_CARI_ADM, name=u'frm_cari_adm',
              parent=prnt, pos=wx.Point(522, 202), size=wx.Size(361, 445),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Sistem Pencarian Data Administrasi')
        self.SetClientSize(wx.Size(361, 445))

    def __init__(self, parent):
        self._init_ctrls(parent)
