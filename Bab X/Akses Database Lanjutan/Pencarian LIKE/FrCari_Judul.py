#Boa:Frame:Frame1

import wx, MySQLdb

conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="akses_database")
cur = conn.cursor()

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1LC, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1TMB_CARI, wxID_FRAME1TXTCARI_JUDUL, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_coll_lc_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='Kode Buku', width=85)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Judul',
              width=232)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading='Penulis', width=114)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Penerbit', width=101)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(393, 232), size=wx.Size(611, 367),
              style=wx.DEFAULT_FRAME_STYLE,
              title='Pencarian Judul Buku dengan Parameter LIKE')
        self.SetClientSize(wx.Size(595, 329))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(595, 329),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Cari Judul', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 24), size=wx.Size(48, 13), style=0)

        self.txtcari_judul = wx.TextCtrl(id=wxID_FRAME1TXTCARI_JUDUL,
              name='txtcari_judul', parent=self.panel1, pos=wx.Point(118, 19),
              size=wx.Size(312, 21), style=0, value='')

        self.tmb_Cari = wx.Button(id=wxID_FRAME1TMB_CARI, label='Cari',
              name='tmb_Cari', parent=self.panel1, pos=wx.Point(448, 16),
              size=wx.Size(75, 23), style=0)
        self.tmb_Cari.Bind(wx.EVT_BUTTON, self.OnTmb_CariButton,
              id=wxID_FRAME1TMB_CARI)

        self.lc = wx.ListCtrl(id=wxID_FRAME1LC, name='lc', parent=self.panel1,
              pos=wx.Point(16, 64), size=wx.Size(544, 256), style=wx.LC_REPORT)
        self._init_coll_lc_Columns(self.lc)

    def __init__(self, parent):
        self._init_ctrls(parent)
    def Isi_List (self) :
        self.lc.DeleteAllItems()
        sql = "select * from buku where judul LIKE '%%%s%%'"%(self.txtcari_judul.GetValue())
        cur.execute(sql)
        hasil= cur.fetchall()
        k =self.lc.GetItemCount()
        for i in hasil :
            self.lc.InsertStringItem(k,"%s"%i[0])
            self.lc.SetStringItem(k,1,"%s"%i[1])
            self.lc.SetStringItem(k,2,"%s"%i[2])
            self.lc.SetStringItem(k,3,"%s"%i[3])
            k = k + 1


    def OnTmb_CariButton(self, event):
       self.Isi_List()       
