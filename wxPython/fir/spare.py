# -*- coding: utf-8 -*-

"""
    Spare.py is a starting point for a wxPython programe
"""


import wx


class Frame(wx.Frame):
    """docstring for Frame"""

    pass


class App(wx.App):
    """docstring for App"""

    def OnInit(self):
        self.frame = Frame(parent=None, title='Spare')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()
