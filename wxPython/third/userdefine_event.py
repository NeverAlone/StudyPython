# -*- coding: utf-8 -*-

"""
    用户自定义事件
    创建自定义事件的步骤：
    1、定义一个新的事件类，它是wxPython的wx.PyEvent类的子类。如果你
想这个事件被作为命令事件，你可以创建wx.PyCommandEvent的子类。像许多
wxPython中的覆盖一样，一个类的py版本使得wxWidget系统明白用Python写的
覆盖C++方法的方法。

    2、创建一个事件类型和一个绑定器对象去绑定该事件到特定的对象。

    3、添加能够建造这个新事件实例的代码，并且使用ProcessEvent()方法将
这个实例引入事件处理系统。一旦该事件被创建，你就可以像使用其它的
wxPython事件一样创建绑定和处理器方法。
"""
import wx


class TwoButtonEvent(wx.PyCommandEvent):  # 1、定义事件
    """docstring for TwoButtonEvent"""

    def __init__(self, evtType, id):
        wx.PyCommandEvent.__init__(self, evtType, id)
        self.clickCount = 0

    def GetClickCount(self):
        return self.clickCount

    def SetClickCount(self, count):
        self.clickCount = count

myEVT_TWO_BUTTON = wx.NewEventType()  # 创建一个事件类型
EVT_TWO_BUTTON = wx.PyEventBinder(myEVT_TWO_BUTTON, 1)  # 创建一个绑定器对象


class TwoButtonPanel(wx.Panel):
    """docstring for TwoButtonPanel"""
    def __init__(self, parent, id=-1, leftText='Left', rightText='Right'):
        wx.Panel.__init__(self, parent, id)
        self.leftButton = wx.Button(self, label=leftText)
        self.rightButton = wx.Button(self, label=rightText,
                                     pos=(100, 0))
        self.leftClick = False
        self.rightClick = False
        self.clickCount = 0

    # 下面两行绑定更低级的事件
        self.leftButton.Bind(wx.EVT_LEFT_DOWN, self.OnLeftClick)
        self.rightButton.Bind(wx.EVT_LEFT_DOWN, self.OnRightClick)

    def OnLeftClick(self, event):
        self.leftClick = True
        self.OnClick()
        event.Skip()  # 继续处理

    def OnRightClick(self, event):
        self.rightClick = True
        self.OnClick()
        event.Skip()  # 继续处理

    def OnClick(self):
        self.clickCount += 1
        if self.leftClick and self.rightClick:
            self.leftClick = False
            self.rightClick = False
            evt = TwoButtonEvent(myEVT_TWO_BUTTON, self.GetId())  # 自己定义事件
            evt.SetClickCount(self.clickCount)  # 添加数据到事件
            self.GetEventHandler().ProcessEvent(evt)  # 处理事件


class CustomEventFrame(wx.Frame):
    """docstring for CustomEventFrame"""
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Click Count:0',
                          size=(300, 100))
        panel = TwoButtonPanel(self)
        self.Bind(EVT_TWO_BUTTON, self.OnTowClick, panel)  # 绑定自定义事件

    def OnTowClick(self, event):
        self.SetTitle('Click Count:%s' % event.GetClickCount())

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = CustomEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
