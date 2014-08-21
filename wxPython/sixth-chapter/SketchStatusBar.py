# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-18 09:42:55
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
给框架添加一个简单的状态栏
"""


import wx
from SketchWindow import SketchWindow


class SketchFrame(wx.Frame):

    """docstring for SketchFrame"""

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Sketch Frame",
                          size=(800, 600))
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchWindow)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])

    def OnSketchWindow(self, event):
        self.statusbar.SetStatusText(
            "Pos: %s" % str(event.GetPositionTuple()), 0)
        self.statusbar.SetStatusText(
            "Current Pts: %s" % len(self.sketch.curLine), 1)
        self.statusbar.SetStatusText(
            "Line Count: %s" % len(self.sketch.lines), 2)
        event.Skip()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = SketchFrame(None)
    frame.Show()
    app.MainLoop()

# This is the end
