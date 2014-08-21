# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-19 09:50:39
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
通用图标
"""


import wx
import wx.lib.buttons as buttons


class GenericButtonFrame(wx.Frame):

    """docstring for GenericButtonFr"""

    def __init__(self):
        super(GenericButtonFrame, self).__init__(None, -1,
                                                 "Generic Button Example",
                                                 size=(500, 350))
        panel = wx.Panel(self, -1)

        sizer = wx.FlexGridSizer(3, 4, 4)
        b = wx.Button(panel, -1, "A wx.Button")
        b.SetDefault()
        sizer.Add(b)

        b = wx.Button(panel, -1, "non-default wx.Button")
        sizer.Add(b)
        sizer.Add((10, 10))

        b = buttons.GenButton(panel, -1, 'Generic Button')
        sizer.Add(b)

        b = buttons.GenButton(panel, -1, 'disabled Generic Button')
        b.Enable(False)
        sizer.Add(b)

        b = buttons.GenButton(panel, -1, "Bigger")
        b.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD, False))
        b.SetBezelWidth(5)
        b.SetBackgroundColour("Navy")
        b.SetForegroundColour("White")
        b.SetToolTipString("This is a BIG Button...")
        sizer.Add(b)

        bmp = wx.Image("IIPP.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()

        b = buttons.GenBitmapButton(panel, -1, bmp)
        sizer.Add(b)

        b = buttons.GenBitmapToggleButton(panel, -1, bmp)
        sizer.Add(b)

        b = buttons.GenBitmapTextButton(panel, -1, bmp, "Bitmapped Text",
                                        size=(175, 75))
        b.SetUseFocusIndicator(False)
        sizer.Add(b)

        b = buttons.GenToggleButton(panel, -1, "Toggle Butoon")
        sizer.Add(b)

        panel.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = GenericButtonFrame()
    frame.Show()
    app.MainLoop()


# This is the end
