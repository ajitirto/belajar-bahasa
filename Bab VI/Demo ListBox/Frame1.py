#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1LIST_KOTA, 
 wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1TXT_KOTA, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(461, 269), size=wx.Size(400, 325),
              style=wx.DEFAULT_FRAME_STYLE, title='Demo ListBox')
        self.SetClientSize(wx.Size(384, 287))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 287),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(206, 206, 206))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Daftar Nama Kota', name='staticText1', parent=self.panel1,
              pos=wx.Point(24, 32), size=wx.Size(87, 13), style=0)

        self.list_kota = wx.ListBox(choices=['Bandung', 'Medan', 'Solo',
              'Surabaya', 'Jakarta'], id=wxID_FRAME1LIST_KOTA, name='list_kota',
              parent=self.panel1, pos=wx.Point(16, 56), size=wx.Size(128, 168),
              style=0)
        self.list_kota.Bind(wx.EVT_LISTBOX, self.OnList_kotaListbox,
              id=wxID_FRAME1LIST_KOTA)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label='Bersihkan ListBox', name='button1', parent=self.panel1,
              pos=wx.Point(24, 248), size=wx.Size(120, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Kota yang Dipilih', name='staticText2', parent=self.panel1,
              pos=wx.Point(184, 88), size=wx.Size(80, 13), style=0)

        self.txt_kota = wx.TextCtrl(id=wxID_FRAME1TXT_KOTA, name='txt_kota',
              parent=self.panel1, pos=wx.Point(184, 112), size=wx.Size(128, 21),
              style=0, value='')

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label='Isi ListBox',
              name='button2', parent=self.panel1, pos=wx.Point(192, 248),
              size=wx.Size(128, 23), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnList_kotaListbox(self, event):
        self.txt_kota.SetValue\
        (self.list_kota.GetStringSelection())

    def OnButton1Button(self, event):
        self.list_kota.Clear()

    def OnButton2Button(self, event):
        self.list_kota.Clear()
        self.list_kota.Append('Bandung')
        self.list_kota.Append('Medan')
        self.list_kota.Append('Solo')
        self.list_kota.Append('Surabaya')
        self.list_kota.Append('Jakarta')
        
