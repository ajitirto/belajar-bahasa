#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frmBuku

modules ={u'frmBuku': [1, 'Main frame of Application', u'frmBuku.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frmBuku.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
