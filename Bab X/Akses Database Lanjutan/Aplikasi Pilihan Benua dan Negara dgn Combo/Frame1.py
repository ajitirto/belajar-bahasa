#Boa:Frame:Frame1

import wx, MySQLdb

conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="akses_database")
cur = conn.cursor()

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1CMB_BENUA, wxID_FRAME1CMB_NEGARA, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(868, 198), size=wx.Size(329, 200),
              style=wx.DEFAULT_FRAME_STYLE, title='Pilihan Benua dan Negara')
        self.SetClientSize(wx.Size(313, 162))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(313, 162),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(192, 192, 192))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Benua', name='staticText1', parent=self.panel1,
              pos=wx.Point(32, 24), size=wx.Size(31, 13), style=0)

        self.cmb_benua = wx.ComboBox(choices=[], id=wxID_FRAME1CMB_BENUA,
              name='cmb_benua', parent=self.panel1, pos=wx.Point(136, 24),
              size=wx.Size(130, 21), style=0, value='')
        self.cmb_benua.SetLabel('')
        self.cmb_benua.Bind(wx.EVT_COMBOBOX, self.OnCmb_benuaCombobox,
              id=wxID_FRAME1CMB_BENUA)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Negara', name='staticText2', parent=self.panel1,
              pos=wx.Point(32, 88), size=wx.Size(36, 13), style=0)

        self.cmb_negara = wx.ComboBox(choices=[], id=wxID_FRAME1CMB_NEGARA,
              name='cmb_negara', parent=self.panel1, pos=wx.Point(136, 80),
              size=wx.Size(130, 21), style=0, value='')
        self.cmb_negara.SetLabel('')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.Isi_Combo_Benua()
    def Isi_Combo_Benua (self) :
        self.cmb_benua.Clear
        sql = " select distinct(benua) from benua_negara "
        cur.execute(sql)
        hasil= cur.fetchall()
        if cur.rowcount > 0 :
            for k in hasil:
                self.cmb_benua.Append(k[0])
    def Isi_Combo_Negara(self) :
        self.cmb_negara.Clear()
        benua = self.cmb_benua.GetStringSelection()
        sql = "select distinct(negara) from benua_negara where \
        benua ='%s' "%(benua)
        cur.execute(sql)
        hasil= cur.fetchall()
        if cur.rowcount > 0 :
            for k in hasil:
                self.cmb_negara.Append(k[0])

    def OnCmb_benuaCombobox(self, event):
        self.Isi_Combo_Negara()

            
        
