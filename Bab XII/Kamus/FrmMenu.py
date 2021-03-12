#Boa:Frame:Frame1

import wx, FrmInput, FrmKamus

def create(parent):
    return Frame1(parent)

[wxID_FRAME1] = [wx.NewId() for _init_ctrls in range(1)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(-4, -4), size=wx.Size(1032, 746),
              style=wx.DEFAULT_FRAME_STYLE, title='Menu Utama')
        self.SetClientSize(wx.Size(1024, 712))

    def __init__(self, parent):
        self._init_ctrls(parent)
        menuBar = wx.MenuBar()
        menuData =wx.Menu()
        menuData.Append(1,"&Isi Data")
        menuData.AppendSeparator()
        menuData.Append(2,"&Keluar")
        menuLihat = wx.Menu()
        menuLihat.Append(3,"&Lihat Kamus")
        menuBar.Append(menuData,"&Data")
        menuBar.Append(menuLihat,"&Kamus")
        self.SetMenuBar(menuBar)
        
        self.Bind(wx.EVT_MENU, self.OnInput, id =1)
        self.Bind(wx.EVT_MENU, self.OnKeluar, id =2)
        self.Bind(wx.EVT_MENU, self.OnLihat, id =3)

    def OnInput(self,event) :
        self.main = FrmInput.create(None)
        self.main.Show()
    def OnKeluar (self,event) :
        self.Destroy()
    def OnLihat (self,event) :
        self.main = FrmKamus.create(None)
        self.main.Show()
            
          
        
