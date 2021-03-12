#Boa:Frame:Frame1

import wx, MySQLdb

conn=MySQLdb.connect(host="localhost",\
user="root",passwd="",db="Akademik")
cur = conn.cursor()

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1LC, wxID_FRAME1PANEL1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class Frame1(wx.Frame):
    def _init_coll_lc_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='NIM',
              width=100)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT, heading='Nama',
              width=240)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(10, 275), size=wx.Size(400, 336),
              style=wx.DEFAULT_FRAME_STYLE, title='Menampilkan Data Mahasiswa')
        self.SetClientSize(wx.Size(384, 298))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 298),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(201, 201, 201))

        self.lc = wx.ListCtrl(id=wxID_FRAME1LC, name='lc', parent=self.panel1,
              pos=wx.Point(8, 8), size=wx.Size(368, 192), style=wx.LC_REPORT)
        self._init_coll_lc_Columns(self.lc)

    def __init__(self, parent):
        self._init_ctrls(parent)
        sql = " select * from mhs "
        cur.execute(sql)
        hasil= cur.fetchall()
        k =self.lc.GetItemCount()
        for i in hasil :
            self.lc.InsertStringItem(k,"%s"%i[0])
            self.lc.SetStringItem(k,1,"%s"%i[1])
            k = k + 1
