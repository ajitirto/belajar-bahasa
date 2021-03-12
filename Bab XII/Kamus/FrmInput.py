#Boa:Frame:Frame1

import wx, MySQLdb
# Buat koneksi
conn =MySQLdb.connect(host="localhost",user="root",passwd="",db = "kamus")
# Buat kursor
kursor = conn.cursor()



def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1LC, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1TMBBERSIH, wxID_FRAME1TMBHAPUS, 
 wxID_FRAME1TMBSIMPAN, wxID_FRAME1TXT_INGGRIS, wxID_FRAME1TXT_MADURA, 
] = [wx.NewId() for _init_ctrls in range(10)]

class Frame1(wx.Frame):
    def _init_coll_lc_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading='Madura',
              width=150)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Inggris', width=192)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(408, 201), size=wx.Size(408, 487),
              style=wx.DEFAULT_FRAME_STYLE, title='Input Kata ')
        self.SetClientSize(wx.Size(392, 449))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Tahoma'))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(392, 449),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Madura', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 40), size=wx.Size(52, 19), style=0)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.txt_madura = wx.TextCtrl(id=wxID_FRAME1TXT_MADURA,
              name='txt_madura', parent=self.panel1, pos=wx.Point(112, 32),
              size=wx.Size(176, 32), style=wx.TE_PROCESS_ENTER, value='')
        self.txt_madura.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))
        self.txt_madura.Bind(wx.EVT_TEXT_ENTER, self.OnTxt_maduraTextEnter,
              id=wxID_FRAME1TXT_MADURA)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Inggris', name='staticText2', parent=self.panel1,
              pos=wx.Point(24, 112), size=wx.Size(50, 19), style=0)
        self.staticText2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.txt_inggris = wx.TextCtrl(id=wxID_FRAME1TXT_INGGRIS,
              name='txt_inggris', parent=self.panel1, pos=wx.Point(112, 112),
              size=wx.Size(176, 32), style=0, value='')
        self.txt_inggris.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.tmbSimpan = wx.Button(id=wxID_FRAME1TMBSIMPAN, label='&Simpan',
              name='tmbSimpan', parent=self.panel1, pos=wx.Point(24, 184),
              size=wx.Size(88, 32), style=0)
        self.tmbSimpan.Bind(wx.EVT_BUTTON, self.OnTmbSimpanButton,
              id=wxID_FRAME1TMBSIMPAN)

        self.tmbBersih = wx.Button(id=wxID_FRAME1TMBBERSIH, label='Bersih',
              name='tmbBersih', parent=self.panel1, pos=wx.Point(144, 184),
              size=wx.Size(75, 32), style=0)
        self.tmbBersih.Bind(wx.EVT_BUTTON, self.OnTmbBersihButton,
              id=wxID_FRAME1TMBBERSIH)

        self.tmbHapus = wx.Button(id=wxID_FRAME1TMBHAPUS, label='Hapus',
              name='tmbHapus', parent=self.panel1, pos=wx.Point(256, 184),
              size=wx.Size(75, 32), style=0)
        self.tmbHapus.Bind(wx.EVT_BUTTON, self.OnTmbHapusButton,
              id=wxID_FRAME1TMBHAPUS)

        self.lc = wx.ListCtrl(id=wxID_FRAME1LC, name='lc', parent=self.panel1,
              pos=wx.Point(24, 240), size=wx.Size(352, 176),
              style=wx.LC_REPORT)
        self._init_coll_lc_Columns(self.lc)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnLcListItemSelected,
              id=wxID_FRAME1LC)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.Isi_List()

    def Isi_List(self) :
        self.lc.DeleteAllItems()
        sql = " select * from kata order by madura"
        kursor.execute(sql)
        hasil = kursor.fetchall()
        baris = self.lc.GetItemCount()
        for i in hasil :
            self.lc.InsertStringItem(baris,"%s"%i[0])
            self.lc.SetStringItem(baris,1,"%s"%i[1])
            baris =baris + 1
          
    def OnTmbSimpanButton(self, event):
        sql = " select * from kata where madura ='%s'" %(self.txt_madura.GetValue())
        kursor.execute(sql)
        hasil = kursor.fetchall()
        if kursor.rowcount > 0 :
           sql1 = "update kata set inggris = '%s' where madura ='%s' "%(self.txt_inggris.GetValue(),self.txt_madura.GetValue())
           kursor.execute(sql1)
           conn.commit()
        else :
           sql1 = "insert into kata (madura,inggris) values ('%s','%s') " %(self.txt_madura.GetValue(),self.txt_inggris.GetValue())
           kursor.execute(sql1)
           conn.commit()
        self.Bersih()
        self.Isi_List()       
    def Bersih(self) :
        self.txt_madura.SetValue("")
        self.txt_inggris.SetValue("")
        self.txt_madura.SetFocus() 

    def OnTmbBersihButton(self, event):
        self.Bersih()

    def OnTmbHapusButton(self, event):
        sql1 = "delete from buku where madura ='%s' "%(self.txt_madura.GetValue())
        kursor.execute(sql1)
        conn.commit()
        self.Bersih()

    def OnLcListItemSelected(self, event):
        self.a = event.m_itemIndex
        md1 = self.lc.GetItem(self.a,0).GetText()
        self.txt_madura.SetValue(md1)
        ing1 = self.lc.GetItem(self.a,1).GetText()
        self.txt_inggris.SetValue(ing1)   

    def OnTxt_maduraTextEnter(self, event):
        sql = "select * from kata where madura ='%s' "%(self.txt_madura.GetValue())
        kursor.execute(sql)
        if kursor.rowcount > 0 :
            hasil = kursor.fetchall()
            for i in hasil :
                self.txt_inggris.SetValue(i[1])
        else :
            self.pesan = wx.MessageDialog(self, "terjemahan kata "+self.txt_inggris.GetValue()+ " tidak ada","Informasi",wx.OK)
            self.pesan.ShowModal()  
        
