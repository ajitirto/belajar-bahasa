#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import FrMenu_Utama

modules ={u'FrMenu_Utama': [1, 'Main frame of Application', u'FrMenu_Utama.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = FrMenu_Utama.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
