# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-15 20:27:02
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
wxPython重构
"""

import wx


class RefactorExample(wx.Frame):

    """
    wxPython重构,框架类
    """

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Refactor Example',
                          size=(340, 200))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("White")
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.createMenuBar()  # 简化的init方法
        self.createButtonBar(panel)
        self.createTextFields(panel)

    def menuData(self):  # 菜单数据
        return (("&File",
               ("&Open", "Open in status bar", self.OnOpen),
            ("&Quit", "Quit", self.OnCloseWindow)),
            ("&Edit",
                ("&Copy", "Copy", self.OnCopy),
                ("&Cut", "Cut", self.OnCut),
                ("&Paste", "Paste", self.OnPaste),
                ("", "", ""),
                ("&Options...", "DispalyOptions", self.OnOptions)))

    # 创建菜单
    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1:]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachLabel, eachStatus, eachHandler in menuData:
            if not eachLabel:
                menu.AppendSeparator()
                continue
            mneuItem = menu.Append(-1, eachLabel, eachStatus)
            self.Bind(wx.EVT_MENU, eachHandler, mneuItem)
        return menu

    def buttonData(self):
        return(("First", self.OnFirst),
              ("PREV", self.OnPrev),
              ("Next", self.OnNext),
              ("Last", self.OnLast))

    def createButtonBar(self, panel, yPos=0):
        xPos = 0
        for eachLabel, eachHandler in self.buttonData():
            pos = (xPos, yPos)
            button = self.buildOneButtton(panel, eachLabel, eachHandler, pos)
            xPos += button.GetSize().width

    def buildOneButtton(self, parent, label, handler, pos=(0, 0)):
        button = wx.Button(parent, -1, label, pos)
        self.Bind(wx.EVT_BUTTON, handler, button)
        return button

    def textFieldData(self):  # 文本数据
        return(("First Name", (10, 50)),
              ("Last Name", (10, 80)))

    # 创建文本
    def createTextFields(self, panel):
        for eachLabel, eachPos in self.textFieldData():
            self.createCaptionedText(panel, eachLabel, eachPos)

    def createCaptionedText(self, panel, label, pos):
        static = wx.StaticText(panel, wx.NewId(), label, pos)
        static.SetBackgroundColour("White")
        textPos = (pos[0] + 75, pos[1])
        wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1), pos=textPos)

    # 空的事件处理器
    def OnPrev(self, event):
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
    frame = RefactorExample(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

# This is the end
