# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-14 18:52:31
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
wxPython pyCrust
spare.py is a starting point for simple wxPython programs.
"""


import wx


class Frame(wx.Frame):

    """
    docstring for Frame
    """
    pass


class App(wx.App):

    """
    asbdh
    """

    def OnInit(self):
        self.frame = wx.Frame(parent=None, id=-1, title='spare')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()

# This is the end
