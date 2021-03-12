#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1LC, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1TMBTAMBAH, wxID_FRAME1TXT_ALAMAT, 
 wxID_FRAME1TXT_NAMA, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame1(wx.Frame):
    def _init_coll_lc_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Nama Lengkap', width=135)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Alamat',
              width=159)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(413, 267), size=wx.Size(486, 352),
              style=wx.DEFAULT_FRAME_STYLE, title='Demo wxListCtrl')
        self.SetClientSize(wx.Size(470, 314))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(470, 314),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(202, 202, 202))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Nama', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 48), size=wx.Size(28, 13), style=0)

        self.txt_nama = wx.TextCtrl(id=wxID_FRAME1TXT_NAMA, name='txt_nama',
              parent=self.panel1, pos=wx.Point(24, 72), size=wx.Size(128, 21),
              style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Alamat', name='staticText2', parent=self.panel1,
              pos=wx.Point(216, 48), size=wx.Size(34, 13), style=0)

        self.txt_alamat = wx.TextCtrl(id=wxID_FRAME1TXT_ALAMAT,
              name='txt_alamat', parent=self.panel1, pos=wx.Point(168, 72),
              size=wx.Size(152, 21), style=0, value='')

        self.tmbTambah = wx.Button(id=wxID_FRAME1TMBTAMBAH, label='Tambah',
              name='tmbTambah', parent=self.panel1, pos=wx.Point(344, 72),
              size=wx.Size(75, 23), style=0)
        self.tmbTambah.Bind(wx.EVT_BUTTON, self.OnTmbTambahButton,
              id=wxID_FRAME1TMBTAMBAH)

        self.lc = wx.ListCtrl(id=wxID_FRAME1LC, name='lc', parent=self.panel1,
              pos=wx.Point(24, 112), size=wx.Size(296, 192),
              style=wx.LC_REPORT)
        self._init_coll_lc_Columns(self.lc)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnLcListItemSelected,
              id=wxID_FRAME1LC)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTmbTambahButton(self, event):
        # Hitung Jumlah Baris
        jml_baris =self.lc.GetItemCount()
        # Isikan nama ke kolom paling kiri
        self.lc.InsertStringItem(jml_baris,\
        self.txt_nama.GetValue())
        # Isikan alamat ke kolom ke-2 
        self.lc.SetStringItem(jml_baris,1,\
        self.txt_alamat.GetValue())
        # counter jumlah baris naik 1 
        jml_baris = jml_baris + 1
        # Bersihkan Isian TextCtrl
        self.txt_nama.SetValue("")
        self.txt_alamat.SetValue("")
        # Focuskan kursor mouse ke txt_nama
        self.txt_nama.SetFocus() 

    def OnLcListItemSelected(self, event):
        no_baris = event.m_itemIndex
        nama = self.lc.GetItem(no_baris,0).GetText()
        alamat = self.lc.GetItem(no_baris,1).GetText()
        self.txt_nama.SetValue(nama)
        self.txt_alamat.SetValue(alamat)
        

