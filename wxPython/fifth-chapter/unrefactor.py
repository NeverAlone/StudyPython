# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-15 16:26:54
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
wxPython: example of refactor
"""

import wx


class UNRefactorExample(wx.Frame):

    """
    """

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Refactor Example',
                          size=(300, 400))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("White")
        prevButton = wx.Button(panel, -1, "<<PREV", pos=(80, 0))
        self.Bind(wx.EVT_BUTTON, self.OnPre, prevButton)
        nextButton = wx.Button(panel, -1, "NEXT>>", pos=(160, 0))
        self.Bind(wx.EVT_BUTTON, self.OnNext, nextButton)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        menuBar = wx.MenuBar()
        menul = wx.Menu()
        openMenuItem = menul.Append(-1, "&Open", "Copy in status bar")
        self.Bind(wx.EVT_MENU, self.OnOpen, openMenuItem)
        quitMenuItem = menul.Append(-1, "&Quit", "Quit")
        self.Bind(wx.EVT_MENU, self.OnClose, quitMenuItem)
        menuBar.Append(menul, u"&文件")
        menu2 = wx.Menu()
        copyItem = menu2.Append(-1, "&Copy", "Copy")
        self.Bind(wx.EVT_MENU, self.OnCopy, copyItem)
        cutItem = menu2.Append(-1, "&Cut", "Cut")
        self.Bind(wx.EVT_MENU, self.OnCut, cutItem)
        pastItem = menu2.Append(-1, "&Paste", "Past")
        self.Bind(wx.EVT_MENU, self.OnPaste, pastItem)
        menuBar.Append(menu2, "&Edit")
        self.SetMenuBar(menuBar)

        static = wx.StaticText(panel, -1, "First Name",
                               pos=(10, 50))
        static.SetBackgroundColour("White")
        text = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                           pos=(80, 50))

        static2 = wx.StaticText(panel, wx.NewId(), "Last Name",
                                pos=(10, 80))
        static2.SetBackgroundColour("White")
        text2 = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                            pos=(80, 80))

        firstButton = wx.Button(panel, -1, "FIRST")
        self.Bind(wx.EVT_BUTTON, self.OnFirst, firstButton)

        menu2.AppendSeparator()
        optItem = menu2.Append(-1, "&Options...", "Display Options")
        self.Bind(wx.EVT_MENU, self.OnOptions, optItem)

        lastButton = wx.Button(panel, -1, "LAST", pos=(240, 0))
        self.Bind(wx.EVT_BUTTON, self.OnLast, lastButton)

    # Just grouping the empty event handlers together

    def OnPre(self, event):
        pass

    def OnClose(self, event):
        pass

    def OnNext(self, event):
        pass

    def OnLast(self, event):
        pass

    def OnFirst(self, event):
        pass

    def OnOpen(self, event):
        pass

    def OnCopy(self, event):
        pass

    def OnCut(self, event):
        pass

    def OnPaste(self, event):
        pass

    def OnOptions(self, event):
        pass

    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = UNRefactorExample(parent=None, id=-1)
    frame.Show()
    app.MainLoop()


# This is the end
