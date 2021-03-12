#Boa:Frame:Frame1

import wx, MySQLdb
# Buat koneksi
conn =MySQLdb.connect(host="localhost",user="root",passwd="",db = "kamus")
# Buat kursor
kursor = conn.cursor()


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1RINGGRIS, wxID_FRAME1RMADURA, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1TMBTERJEMAHKAN, 
 wxID_FRAME1TXT_KATA, wxID_FRAME1TXT_TERJEMAHAN, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(385, 232), size=wx.Size(484, 350),
              style=wx.DEFAULT_FRAME_STYLE,
              title='Kamus Madura Inggris dan Inggris Madura')
        self.SetClientSize(wx.Size(468, 312))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(468, 312),
              style=wx.TAB_TRAVERSAL)

        self.rMadura = wx.RadioButton(id=wxID_FRAME1RMADURA,
              label='Madura-Inggris', name='rMadura', parent=self.panel1,
              pos=wx.Point(24, 40), size=wx.Size(152, 24), style=0)
        self.rMadura.SetValue(True)
        self.rMadura.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Tahoma'))

        self.rInggris = wx.RadioButton(id=wxID_FRAME1RINGGRIS,
              label='Inggris-Madura', name='rInggris', parent=self.panel1,
              pos=wx.Point(264, 40), size=wx.Size(136, 24), style=0)
        self.rInggris.SetValue(False)
        self.rInggris.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Tahoma'))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Masukkan Kata yang Dicari', name='staticText1',
              parent=self.panel1, pos=wx.Point(32, 104), size=wx.Size(188, 19),
              style=0)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.txt_kata = wx.TextCtrl(id=wxID_FRAME1TXT_KATA, name='txt_kata',
              parent=self.panel1, pos=wx.Point(32, 136), size=wx.Size(224, 32),
              style=0, value='')
        self.txt_kata.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Tahoma'))

        self.tmbTerjemahkan = wx.Button(id=wxID_FRAME1TMBTERJEMAHKAN,
              label='Terjemahkan', name='tmbTerjemahkan', parent=self.panel1,
              pos=wx.Point(280, 136), size=wx.Size(96, 23), style=0)
        self.tmbTerjemahkan.Bind(wx.EVT_BUTTON, self.OnTmbTerjemahkanButton,
              id=wxID_FRAME1TMBTERJEMAHKAN)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Terjemahan', name='staticText2', parent=self.panel1,
              pos=wx.Point(40, 192), size=wx.Size(85, 19), style=0)
        self.staticText2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.txt_terjemahan = wx.TextCtrl(id=wxID_FRAME1TXT_TERJEMAHAN,
              name='txt_terjemahan', parent=self.panel1, pos=wx.Point(40, 224),
              size=wx.Size(216, 32), style=0, value='')
        self.txt_terjemahan.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTmbTerjemahkanButton(self, event):
        if self.rMadura.Value == True :
            sql = "select * from kata where madura ='%s' "%(self.txt_kata.GetValue())
            kursor.execute(sql)
            if kursor.rowcount > 0 :
              hasil = kursor.fetchall()
              for i in hasil :
                self.txt_terjemahan.SetValue(i[1])
            else :
              self.pesan = wx.MessageDialog(self, "terjemahan kata "+self.txt_kata.GetValue()+ " tidak ada","Informasi",wx.OK)
              self.pesan.ShowModal()  
        else :
            sql = "select * from kata where inggris ='%s' "%(self.txt_kata.GetValue())
            kursor.execute(sql)
            if kursor.rowcount > 0 :
              hasil = kursor.fetchall()
              for i in hasil :
                self.txt_terjemahan.SetValue(i[0])
            else :
              self.pesan = wx.MessageDialog(self, "terjemahan kata "+self.txt_kata.GetValue()+ " tidak ada","Informasi",wx.OK)
              self.pesan.ShowModal()  
                             
