# -*- coding: utf-8 -*-

"""
    Bind(event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY)
"""

import wx


class InsertFrame(wx.Frame):
    """docstring for InsertFr"""
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame With Button',
                          size=(300, 100))

        panel = wx.Panel(self, -1)  # 创建画板
        button = wx.Button(panel, label='Close', pos=(130, 15),
                           size = (40, 40))  # 将按钮添加到画板
        # 绑定按钮的单击事件
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)

        # 绑定窗口的关闭事件
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseMe(self, event):
        self.Close(False)

    def OnCloseWindow(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = InsertFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

# This is the end
