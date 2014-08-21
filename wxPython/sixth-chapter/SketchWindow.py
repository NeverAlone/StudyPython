# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-18 07:30:57
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
初始的SketchWindow代码
"""


import wx


class SketchWindow(wx.Window):

    """docstring for SketchWindow"""

    def __init__(self, parent, ID):
        wx.Window.__init__(self, parent, ID)
        self.SetBackgroundColour("White")
        self.color = "Black"
        self.thickness = 1
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)  # 创建一个wx.Pen对象

        self.lines = []
        self.curLine = []
        self.pos = (0, 0)
        self.InitBuffer()
        self.count = 0

    # 连接事件
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_RIGHT_DCLICK, self.OnRightDClick)

    def OnRightDClick(self, event):
        if self.count % 2 == 0:
            self.SetColor("Blue")
        else:
            self.SetColor("Red")
        self.count += 1
        if self.count > 256:
            self.color = 0

    def InitBuffer(self):
        size = self.GetClientSize()
    # 创建一个缓存的设备上下文
        self.buffer = wx.EmptyBitmap(size.width, size.height)
        dc = wx.BufferedDC(None, self.buffer)
    # 使用设备上下文
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        self.DrawLines(dc)

        self.reInitBuffer = False

    def GetLinesData(self):
        return self.lines[:]

    def SetLinesData(self, lines):
        self.lines = lines[:]
        self.InitBuffer()
        self.Refresh()

    def OnLeftDown(self, event):
        # print "Mouse Down"
        self.curLine = []
        self.pos = event.GetPositionTuple()  # 得到鼠标位置
        self.CaptureMouse()  # 捕获鼠标

    def OnLeftUp(self, event):
        # print "mouse up"
        if self.HasCapture():
            self.lines.append((self.color,
                               self.thickness,
                               self.curLine))
            self.curLine = []
            self.ReleaseMouse()  # 释放鼠标

    def OnMotion(self, event):
        if event.Dragging() and event.LeftIsDown():  # 确定是否拖动
            # print "mouse dragging"
            dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
            self.drawMotion(dc, event)
        event.Skip()

    # 绘画到设备上下文
    def drawMotion(self, dc, event):
        # print "draw mouse motion"
        dc.SetPen(self.pen)
        newPos = event.GetPositionTuple()
        coords = self.pos + newPos
        self.curLine.append(coords)
        dc.DrawLine(*coords)
        self.pos = newPos

    def OnSize(self, event):
        # print "Window size change"
        self.reInitBuffer = True
        # 处理一个resize事件

    def OnIdle(self, event):  # 空闲时的处理
        if self.reInitBuffer:
            # print "redraw"
            self.InitBuffer()
            self.Refresh(False)

    def OnPaint(self, event):
        # print "handle paint request"
        wx.BufferedPaintDC(self, self.buffer)
        # 处理一个paint请求

    # 绘制所有线条
    def DrawLines(self, dc):
        # print "redraw all the lines"
        for colour, thickness, line in self.lines:
            pen = wx.Pen(colour, thickness, wx.SOLID)
            dc.SetPen(pen)
            for coords in line:
                dc.DrawLine(*coords)

    def SetColor(self, color):
        self.color = color
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)

    def SetThickness(self, num):
        self.thickness = num
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)


class SketchFrame(wx.Frame):

    """docstring for SketchFrame"""

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1,
                          "Sketch Frame", size=(800, 600))
        self.sketch = SketchWindow(self, -1)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = SketchFrame(None)
    frame.Show()
    app.MainLoop()

# This is the end
