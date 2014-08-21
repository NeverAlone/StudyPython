# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-21 14:50:40
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
定义一个模式对话框
"""


import wx


class SubclassDialog(wx.Dialog):

    """docstring for SubclassDialog"""

    def __init__(self):
        super(SubclassDialog, self).__init__(None, -1, "Dialog Subclass",
                                             size=(300, 100))
        okButton = wx.Button(self, wx.ID_OK, "OK", pos=(15, 15))
        # okButton.SetDefault()
        cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel",
                                 pos=(115, 15))
        cancelButton.SetDefault()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    app.MainLoop()
    dialog = SubclassDialog()
    result = dialog.ShowModal()
    if result == wx.ID_OK:
        print "OK"
    else:
        print "Cancel"
    dialog.Destroy()


# This is the end
