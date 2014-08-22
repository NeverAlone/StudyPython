# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-22 11:01:33
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
Validate
"""


import wx

about_txt = """\
The validator used in this example will ensure that the text
controls are not empty when you press the Ok button, and
will not let you leave if any of the Validations fail."""


class NotEmptyValidator(wx.PyValidator):

    """docstring for NotEmptyValidator"""

    def __init__(self):
        super(NotEmptyValidator, self).__init__()

    def Clone(self):
        """
        不是每个验证器都需要 Clone()方法的
        """
        return NotEmptyValidator()

    def Validate(self, win):  # 使用验证器方法
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()

        if len(text) == 0:
            wx.MessageBox("This filed must contain some text", "Error")
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour(
                wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True

    def TransferToWindow(self):
        return True

    def TransferFromWindow():
        return True


class MyDialog(wx.Dialog):

    """docstring for MyDialog"""

    def __init__(self, arg):
        super(MyDialog, self).__init__(None, -1, "Validators: validating")

        about = wx.StaticText(self, -1, about_txt)
        name_l = wx.StaticText(self, -1, "Name:")
        eamil_l = wx.StaticText(self, -1, "Email:")
        phone_l = wx.StaticText(self, -1, "Phone:")

        # 使用验证器
        name_t = wx.TextCtrl(self, validator=NotEmptyValidator())
        eamil_t = wx.TextCtrl(self, validator=NotEmptyValidator())
        phone_t = wx.TextCtrl(self, validator=NotEmptyValidator())

        okay = wx.Button(self, wx.ID_OK)
        okay.SetDefault()
        cancel = wx.Button(self, wx.ID_CANCEL)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(about, 0, wx.All, 5)
        sizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.All, 5)

        fgs = wx.FlexGridSizer(3, 2, 5, 5)
        fgs.Add(name_l, 0, wx.ALIGN_RIGHT)




# This is the end
