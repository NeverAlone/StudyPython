# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-20 10:39:51
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
MDI
"""


import wx


class MDIFrame(wx.MDIParentFrame):

    """docstring for MDIFrame"""

    def __init__(self):
        super(MDIFrame, self).__init__(None, -1, "MDI Frame",
                                       size=(600, 400))
        menu = wx.Menu()
        menu.Append(5000, "&New Window")
        menu.Append(5001, "&Exit")
        menubar = wx.MenuBar()
        menubar.Append(menu, "&File")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnNewWindow, id=5000)
        self.Bind(wx.EVT_MENU, self.OnExit, id=5001)

    def OnExit(self, event):
        self.Close()

    def OnNewWindow(self, event):
        win = wx.MDIChildFrame(self, -1, "Child Window")
        win.Show()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    MDIFrame().Show()
    app.MainLoop()


# This is the end
