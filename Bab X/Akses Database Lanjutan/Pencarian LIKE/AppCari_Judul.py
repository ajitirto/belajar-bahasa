#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import FrCari_Judul

modules ={u'FrCari_Judul': [1, 'Main frame of Application', u'FrCari_Judul.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = FrCari_Judul.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
