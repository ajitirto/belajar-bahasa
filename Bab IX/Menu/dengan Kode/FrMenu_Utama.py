#Boa:Frame:Frame1

import wx,FrEdit,FrGabungan,FrHapus,FrSimpan,FrLihatData,FrCariData

def create(parent):
    return Frame1(parent)

[wxID_FRAME1] = [wx.NewId() for _init_ctrls in range(1)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(-8, -8), size=wx.Size(1382, 744),
              style=wx.DEFAULT_FRAME_STYLE, title='Menu Utama')
        self.SetClientSize(wx.Size(1366, 706))

    def __init__(self, parent):
        self._init_ctrls(parent)
        menuTampil_Data = wx.Menu()
        menuTampil_Data.Append(1, "Tampilkan Data 1 Record")
        menuTampil_Data.Append(2, "Tampilkan Semua Data")
        menuTampil_Data.AppendSeparator()
        menuTampil_Data.Append(3, "Exit")
        menuUbah_Data = wx.Menu()
        menuUbah_Data.Append(4, "Simpan Data")
        menuUbah_Data.Append(5, "Hapus Data")
        menuUbah_Data.Append(6, "Edit Data")
        menuGabungan = wx.Menu()
        menuGabungan.Append(7, "Frame Gabungan")
        menuBar = wx.MenuBar()
        menuBar.Append(menuTampil_Data, "Tampilkan Data")
        menuBar.Append(menuUbah_Data, "Ubah Data")
        menuBar.Append(menuGabungan, "Gabungan")
        self.SetMenuBar(menuBar)
        #Membuat StatusBar
        self.CreateStatusBar()
        #Menuliskan tulisan pada StatusBar
        self.SetStatusText("Selamat Datang di Python!")
        self.Bind(wx.EVT_MENU, self.OnTampil1, id=1)
        self.Bind(wx.EVT_MENU, self.OnTampil_Semua, id=2)
        self.Bind(wx.EVT_MENU, self.OnExit, id=3)
        self.Bind(wx.EVT_MENU, self.OnSimpan_Data, id=4)
        self.Bind(wx.EVT_MENU, self.OnHapus_Data, id=5)
        self.Bind(wx.EVT_MENU, self.OnEdit_Data, id=6)
        self.Bind(wx.EVT_MENU, self.OnGabungan, id=7)
        
    def OnTampil1(self, event):
        self.main = FrCariData.create(None)
        self.main.Show()
    def OnTampil_Semua(self, event):
        self.main = FrLihatData.create(None)
        self.main.Show() 
    
    def OnExit(self, event):
        self.Close()
     
    def OnSimpan_Data(self, event):
        self.main = FrSimpan.create(None)
        self.main.Show()
        
    def OnHapus_Data(self, event):
        self.main = FrHapus.create(None)
        self.main.Show()
    
    def OnEdit_Data(self, event):
        self.main = FrEdit.create(None)
        self.main.Show()
    
    def OnGabungan(self, event):
        self.main = FrGabungan.create(None)
        self.main.Show()

