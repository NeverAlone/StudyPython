# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-19 15:57:45
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
Radio Button
"""


import wx


class RadionButtonFrame(wx.Frame):

    """docstring for RadionButtonFrame"""

    def __init__(self):
        super(RadionButtonFrame, self).__init__(None, -1, 'Radio Example',
                                                size=(200, 200))
        panel = wx.Panel(self, -1)

    # 创建单选按钮
        radio1 = wx.RadioButton(panel, -1, "Elmo", pos=(20, 50),
                                style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, -1, "Ernie", pos=(20, 80))
        radio3 = wx.RadioButton(panel, -1, "Bert", pos=(20, 110))
        radio4 = wx.RadioButton(panel, -1, "danner", pos=(20, 20))

    # 创建文本控件
        text1 = wx.TextCtrl(panel, -1, "", pos=(80, 50))
        text2 = wx.TextCtrl(panel, -1, "", pos=(80, 80))
        text3 = wx.TextCtrl(panel, -1, "", pos=(80, 110))
        self.texts = {"Elmo": text1, "Ernie": text2, "Bert": text3}
        for eachText in [text2, text3]:
            eachText.Enable(False)
        for eachRadio in [radio1, radio2, radio3]:
            self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio, eachRadio)
        self.selectedText = text1

    def OnRadio(self, event):
        if self.selectedText:
            self.selectedText.Enable(False)
        radioSelected = event.GetEventObject()
        text = self.texts[radioSelected.GetLabel()]
        text.Enable(True)
        self.selectedText = text

if __name__ == '__main__':
    app = wx.PySimpleApp()
    RadionButtonFrame().Show()
    app.MainLoop()




# This is the end
