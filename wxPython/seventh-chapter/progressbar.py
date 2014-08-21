# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-19 15:32:11
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
进度条
"""

import wx


class GaugeFrame(wx.Frame):

    """docstring for GaugeFrame"""

    def __init__(self):
        super(GaugeFrame, self).__init__(None, -1, "Gauge Example",
                                         size=(300, 150))

        panel = wx.Panel(self, -1)
        self.count = 0
        self.gauge = wx.Gauge(panel, -1, 50, (20, 50), (250, 25))
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        self.Bind(wx.EVT_IDLE, self.OnIdle)

    def OnIdle(self, event):
        self.count = self.count + 1
        if self.count >= 100:
            self.count = 0
        self.gauge.SetValue(self.count)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    GaugeFrame().Show()
    app.MainLoop()


# This is the end
