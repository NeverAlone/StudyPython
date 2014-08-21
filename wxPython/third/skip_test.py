# -*- coding: utf-8 -*-


import wx


class MouseEventFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Button', size=(300, 100))
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('White')
        self.button = wx.Button(self.panel, label="Not Over", pos=(100, 15))
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow2)
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)

    def OnEnterWindow(self, event):
        self.button.SetLabel('Over Me')
        event.Skip()

    def OnEnterWindow2(self, event):
        self.panel.SetBackgroundColour('Red')
        self.panel.Refresh()

    def OnLeaveWindow(self, event):
        self.button.SetLabel('Not Over')
        self.panel.SetBackgroundColour('White')
        self.panel.Refresh()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MouseEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

# This is the nend
