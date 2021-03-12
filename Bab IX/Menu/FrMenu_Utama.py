#Boa:Frame:Frame1

import wx,FrEdit,FrGabungan,FrHapus,FrSimpan,FrLihatData,FrCariData

def create(parent):
    return Frame1(parent)

[wxID_FRAME1] = [wx.NewId() for _init_ctrls in range(1)]

[wxID_FRAME1MENUTAMPILEXIT, wxID_FRAME1MENUTAMPILTAMPIL1, 
 wxID_FRAME1MENUTAMPILTAMPIL_SEMUA, 
] = [wx.NewId() for _init_coll_menuTampil_Items in range(3)]

[wxID_FRAME1MENUUBAHEDIT, wxID_FRAME1MENUUBAHHAPUS, wxID_FRAME1MENUUBAHSIMPAN, 
] = [wx.NewId() for _init_coll_menuUbah_Items in range(3)]

[wxID_FRAME1MENUGABUNGANGABUNGAN] = [wx.NewId() for _init_coll_menuGabungan_Items in range(1)]

class Frame1(wx.Frame):
    def _init_coll_menuUbah_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MENUUBAHSIMPAN,
              kind=wx.ITEM_NORMAL, text='Simpan Data')
        parent.Append(help='', id=wxID_FRAME1MENUUBAHEDIT, kind=wx.ITEM_NORMAL,
              text='Edit Data')
        parent.Append(help='', id=wxID_FRAME1MENUUBAHHAPUS, kind=wx.ITEM_NORMAL,
              text='Hapus Data')
        self.Bind(wx.EVT_MENU, self.OnMenuUbahSimpanMenu,
              id=wxID_FRAME1MENUUBAHSIMPAN)
        self.Bind(wx.EVT_MENU, self.OnMenuUbahEditMenu,
              id=wxID_FRAME1MENUUBAHEDIT)
        self.Bind(wx.EVT_MENU, self.OnMenuUbahHapusMenu,
              id=wxID_FRAME1MENUUBAHHAPUS)

    def _init_coll_menuTampil_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MENUTAMPILTAMPIL1,
              kind=wx.ITEM_NORMAL, text='Tampilkan Data 1 Record')
        parent.Append(help='', id=wxID_FRAME1MENUTAMPILTAMPIL_SEMUA,
              kind=wx.ITEM_NORMAL, text='Tampilkan Semua Data')
        parent.AppendSeparator()
        parent.Append(help='', id=wxID_FRAME1MENUTAMPILEXIT,
              kind=wx.ITEM_NORMAL, text='Exit')
        self.Bind(wx.EVT_MENU, self.OnMenuTampilTampil1Menu,
              id=wxID_FRAME1MENUTAMPILTAMPIL1)
        self.Bind(wx.EVT_MENU, self.OnMenuTampilTampil_semuaMenu,
              id=wxID_FRAME1MENUTAMPILTAMPIL_SEMUA)
        self.Bind(wx.EVT_MENU, self.OnMenuTampilExitMenu,
              id=wxID_FRAME1MENUTAMPILEXIT)

    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuTampil, title='Tampilkan Data')
        parent.Append(menu=self.menuUbah, title='Ubah Data')
        parent.Append(menu=self.menuGabungan, title='Gabungan')

    def _init_coll_menuGabungan_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MENUGABUNGANGABUNGAN,
              kind=wx.ITEM_NORMAL, text='Frame Gabungan')
        self.Bind(wx.EVT_MENU, self.OnMenuGabunganGabunganMenu,
              id=wxID_FRAME1MENUGABUNGANGABUNGAN)

    def _init_utils(self):
        # generated method, don't edit
        self.menuTampil = wx.Menu(title='')

        self.menuUbah = wx.Menu(title='')

        self.menuGabungan = wx.Menu(title='')

        self.menuBar1 = wx.MenuBar()
        self.menuBar1.SetClientSize(wx.Size(77368304, 27135440))

        self._init_coll_menuTampil_Items(self.menuTampil)
        self._init_coll_menuUbah_Items(self.menuUbah)
        self._init_coll_menuGabungan_Items(self.menuGabungan)
        self._init_coll_menuBar1_Menus(self.menuBar1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(-9, 0), size=wx.Size(1382, 744),
              style=wx.DEFAULT_FRAME_STYLE, title='Menu Utama')
        self._init_utils()
        self.SetClientSize(wx.Size(1366, 706))
        self.Enable(True)
        self.SetMenuBar(self.menuBar1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnMenuTampilTampil1Menu(self, event):
        self.main = FrCariData.create(None)
        self.main.Show()

    def OnMenuTampilTampil_semuaMenu(self, event):
        self.main = FrLihatData.create(None)
        self.main.Show()

    def OnMenuUbahSimpanMenu(self, event):
        self.main = FrSimpan.create(None)
        self.main.Show()

    def OnMenuUbahEditMenu(self, event):
        self.main = FrEdit.create(None)
        self.main.Show()

    def OnMenuUbahHapusMenu(self, event):
        self.main = FrHapus.create(None)
        self.main.Show()

    def OnMenuGabunganGabunganMenu(self, event):
        self.main = FrGabungan.create(None)
        self.main.Show()

    def OnMenuTampilExitMenu(self, event):
        self.Close()
