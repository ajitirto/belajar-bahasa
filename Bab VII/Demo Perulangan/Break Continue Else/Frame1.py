#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1LB_BIASA, wxID_FRAME1LB_PRIMA, wxID_FRAME1PANEL1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
 wxID_FRAME1STATICTEXT4, wxID_FRAME1TMBISI_LISTBOX, wxID_FRAME1TXT_AKHIR, 
 wxID_FRAME1TXT_AWAL, 
] = [wx.NewId() for _init_ctrls in range(11)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(599, 197), size=wx.Size(400, 387),
              style=wx.DEFAULT_FRAME_STYLE,
              title='Demo Break, Else, dan Continue')
        self.SetClientSize(wx.Size(384, 349))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(384, 349),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(196, 196, 196))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Angka Awal', name='staticText1', parent=self.panel1,
              pos=wx.Point(96, 24), size=wx.Size(57, 13), style=0)

        self.txt_awal = wx.TextCtrl(id=wxID_FRAME1TXT_AWAL, name='txt_awal',
              parent=self.panel1, pos=wx.Point(200, 24), size=wx.Size(100, 21),
              style=0, value='')

        self.tmbIsi_ListBox = wx.Button(id=wxID_FRAME1TMBISI_LISTBOX,
              label='Proses', name='tmbIsi_ListBox', parent=self.panel1,
              pos=wx.Point(136, 96), size=wx.Size(88, 23), style=0)
        self.tmbIsi_ListBox.Bind(wx.EVT_BUTTON, self.OnTmbIsi_ListBoxButton,
              id=wxID_FRAME1TMBISI_LISTBOX)

        self.lb_prima = wx.ListBox(choices=[], id=wxID_FRAME1LB_PRIMA,
              name='lb_prima', parent=self.panel1, pos=wx.Point(32, 152),
              size=wx.Size(132, 184), style=0)

        self.lb_biasa = wx.ListBox(choices=[], id=wxID_FRAME1LB_BIASA,
              name='lb_biasa', parent=self.panel1, pos=wx.Point(208, 152),
              size=wx.Size(132, 184), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Bilangan Prima', name='staticText2', parent=self.panel1,
              pos=wx.Point(56, 128), size=wx.Size(70, 13), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label='Bukan Bilangan Prima', name='staticText3',
              parent=self.panel1, pos=wx.Point(224, 128), size=wx.Size(102, 13),
              style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label='Angka Akhir', name='staticText4', parent=self.panel1,
              pos=wx.Point(96, 64), size=wx.Size(58, 13), style=0)

        self.txt_akhir = wx.TextCtrl(id=wxID_FRAME1TXT_AKHIR, name='txt_akhir',
              parent=self.panel1, pos=wx.Point(200, 64), size=wx.Size(100, 21),
              style=0, value='')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnTmbIsi_ListBoxButton(self, event):
        awal = int(self.txt_awal.GetValue())
        akhir = int (self.txt_akhir.GetValue())
        for n in range(awal, akhir) :
            for x in range (awal, n) :
                if n%x == 0 :
                    self.lb_biasa.Append(str(n))
                    break
            else :
                self.lb_prima.Append(str(n))
