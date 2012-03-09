#!/usr/bin/env python
#coding:utf-8

import sys
from frame.main_frame import MainFrame
from config import *

sys.path.append('.')

if __name__ == "__main__":
    mainFrame = MainFrame(SCREENWIDTH, SCREENHEIGHT, TITLETEXT, BACKGROUD, MOUSE)
    mainFrame.run()

