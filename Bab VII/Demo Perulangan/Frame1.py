#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1LB, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1TMBISI_LISTBOX, wxID_FRAME1TXT_AKHIR, 
 wxID_FRAME1TXT_AWAL, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(496, 268), size=wx.Size(400, 317),
              style=wx.DEFAULT_FRAME_STYLE, title='Demo Perulangan')
        self.SetClientSize(wx.Size(384, 279))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 279),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(188, 188, 188))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Angka Awal', name='staticText1', parent=self.panel1,
              pos=wx.Point(32, 24), size=wx.Size(57, 13), style=0)

        self.txt_awal = wx.TextCtrl(id=wxID_FRAME1TXT_AWAL, name='txt_awal',
              parent=self.panel1, pos=wx.Point(32, 48), size=wx.Size(100, 21),
              style=0, value='')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Angka Akhir', name='staticText2', parent=self.panel1,
              pos=wx.Point(168, 24), size=wx.Size(58, 13), style=0)

        self.txt_akhir = wx.TextCtrl(id=wxID_FRAME1TXT_AKHIR, name='txt_akhir',
              parent=self.panel1, pos=wx.Point(160, 48), size=wx.Size(100, 21),
              style=0, value='')

        self.tmbIsi_ListBox = wx.Button(id=wxID_FRAME1TMBISI_LISTBOX,
              label='Isikan pada ListBox', name='tmbIsi_ListBox',
              parent=self.panel1, pos=wx.Point(24, 88), size=wx.Size(112, 23),
              style=0)
        self.tmbIsi_ListBox.Bind(wx.EVT_BUTTON, self.OnTmbIsi_ListBoxButton,
              id=wxID_FRAME1TMBISI_LISTBOX)

        self.lb = wx.ListBox(choices=[], id=wxID_FRAME1LB, name='lb',
              parent=self.panel1, pos=wx.Point(160, 88), size=wx.Size(104, 168),
              style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTmbIsi_ListBoxButton(self, event):
        awal = int(self.txt_awal.GetValue())
        akhir = int(self.txt_akhir.GetValue())
        i = awal
        for i in range (awal,akhir+1) :
            self.lb.Append(str(i))
            
            
