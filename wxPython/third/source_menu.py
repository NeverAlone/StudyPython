# -*- coding: utf-8 -*-

import wx


class MenuEventFrame(wx.Frame):
    """docstring for MenuEventFrame"""
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Menus',
                          size=(300, 200))
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuItem = menu1.Append(-1, "&Exit...")
        menuBar.Append(menu1, "&File")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.OnCloseMe, menuItem)

    def OnCloseMe(self, event):
        self.Close(True)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MenuEventFrame(None, -1)
    frame.Show()
    app.MainLoop()


# This is the end
