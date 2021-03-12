#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import FrCariData

modules ={u'FrCariData': [1, 'Main frame of Application', u'FrCariData.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = FrCariData.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
