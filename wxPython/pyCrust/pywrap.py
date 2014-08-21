# -*- coding: utf-8 -*-
# uses python2.7.6
# @Date    : 2014-08-14 19:03:55
# @Author  : lonely
# @Link    : http://blog.csdn.net/zc937533415
# @Version : $Id$


"""
	PyWrap is a command line utility that runs a python
	program with additional runtime tools,such as PyCrust
"""

import os
import sys
import wx
from wx.py.crust import CrustFrame


def wrap(app):
    wx.InitAllImageHandlers()
    frame = CrustFrame()
    frame.SetSize((750, 525))
    frame.Show(True)
    frame.shell.interp.locals['app'] = app
    app.MainLoop()


def main(modulename=None):
    sys.path.insert(0, os.curdir)
    if not modulename:
        if len(sys.argv) < 2:
            print "Please specify a module name."
            raise SystemExit
        modulename = sys.argv[1]
    if modulename.endswith('.py'):
        modulename = modulename[:-3]
    module = __import__(modulename)
    # Find the App class.
    App = None
    d = module.__dict__
    for item in d.keys():
        try:
            if issubclass(d[item], wx.App):
                App = d[item]
        except (NameError, TypeError):
            pass
    if App is None:
        print "No App class was Found."
        raise SystemExit
    app = App()
    wrap(app)

if __name__ == '__main__':
    main()

# This is the end
