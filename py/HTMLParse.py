# -*- coding: utf-8 -*-


"""
    python2.7.6
    @lonley
    HTML 解释器
    失败

"""


from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint


class MyHTMLParser(HTMLParser):
    """docstring for MyHTMLParser"""

    def handle_starttag(self, tag):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('/%s' % tag)

    def handle_startendtag(self, tag):
        print('%s/' % tag)

    def handle_data(self, data):
        print("data")

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')

# This is the end
