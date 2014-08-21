# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-19 09:05:32
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
位图按钮
"""


import wx


class BitmapButtonFrame(wx.Frame):

    """docstring for BitmapButtonFrame"""

    def __init__(self):
        super(
            BitmapButtonFrame, self).__init__(None, -1, 'Bitmap Button Example',
                                              size=(200, 150))
        panel = wx.Panel(self, -1)
        bmp = wx.Image("IIPP.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, bmp, pos=(10, 20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()
        self.button2 = wx.BitmapButton(panel, -1, bmp, pos=(100, 20),
                                       style=0)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button2)

    def OnClick(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = BitmapButtonFrame()
    frame.Show()
    app.MainLoop()

# This is the end
