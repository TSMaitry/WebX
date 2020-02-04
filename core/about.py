#!/use/bin/env/python2
#-*- encoding: utf-8 -*-

import os
import sys
import time

# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue

def force_to_unicode(text): 
  "If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding" 
  return text if isinstance(text, unicode) else text.decode('utf8')
print("                       "+R+"WEB"+B+"X")
print(""+B+"┌┈┈┈┈┤"+O+"MIT License"+B+"├┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┐")
print(""+B+"│"+G+"                                                "+B+"│")
print(""+B+"│"+G+"          Copyright (c) 2020 TSMaitry           "+B+"│")
print(""+B+"│"+G+"                                                "+B+"│")
print(""+B+"│"+G+"Permission is hereby granted, free of charge, to"+B+"│")
print(""+B+"│"+G+"any person obtaining a copy of this software and"+B+"│")
print(""+B+"│"+G+"associated documentation files  The Software, to"+B+"│")
print(""+B+"│"+G+"deal in  the    Software    without restriction,"+B+"│")
print(""+B+"│"+G+"including without limitation the rights to  use,"+B+"│")
print(""+B+"│"+G+"copy,  modify,   merge,   publish,    distribute"+B+"│")
print(""+B+"│"+G+"sublicense, and/or sell copies of the  Software,"+B+"│")
print(""+B+"│"+G+"and to permit persons to whom  the  Software  is"+B+"│")
print(""+B+"│"+G+"furnished  to  do  so,  subject to the following"+B+"│")
print(""+B+"│"+G+"conditions:                                     "+B+"│")
print(""+B+"│"+G+"                                                "+B+"│")
print(""+B+"│"+G+"  The above copyright notice and this permission"+B+"│")
print(""+B+"│"+G+"notice  shall  be  included  in  all vcopies  or"+B+"│")
print(""+B+"│"+G+"substantial portions of the Software.           "+B+"│")
print(""+B+"│"+G+"                                                "+B+"│")
print(""+B+"│"+G+"   THE  SOFTWARE  IS  PROVIDED  AS  IS,  WITHOUT"+B+"│")
print(""+B+"│"+G+"WARRANTY   OF  ANY  KIND,  EXPRESS  OR  IMPLIED,"+B+"│")
print(""+B+"│"+G+"INCLUDING  BUT  NOT LIMITED TO THE WARRANTIES OF"+B+"│")
print(""+B+"│"+G+"MERCHANTABILITY,FITNESS FOR A PARTICULAR PURPOSE"+B+"│")
print(""+B+"│"+G+"AND  NONINFRINGEMENT.  IN  NO  EVENT  SHALL  THE"+B+"│")
print(""+B+"│"+G+"AUTHORS HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES"+B+"│")
print(""+B+"│"+G+"OR  OTHER  LIABILITY,  WHETHER  IN  AN ACTION OF"+B+"│")
print(""+B+"│"+G+"CONTRACT, TORT OR OTHERWISE, ARISING FROM,OUT OF"+B+"│")
print(""+B+"│"+G+"OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR"+B+"│")
print(""+B+"│"+G+"OTHER DEALINGS IN THE SOFTWARE.                 "+B+"│")
print(""+B+"├────────────────────────────────────────────────┤")
print(""+B+"│"+G+"       Developed By : Trilok Singh Maitry       "+B+"│")
print(""+B+"│"+G+"          Interface : Command line              "+B+"│")
print(""+B+"│"+G+"             System : GNU/Linux                 "+B+"│")
print(""+B+"│"+G+"             Device : Redmi Note 7 Pro          "+B+"│")
print(""+B+"│"+G+"   Operating System : Android Pie               "+B+"│")
print(""+B+"│"+G+"     Kernel Version : 4.14.81-perf+             "+B+"│")
print(""+B+"│"+G+"  (c) Continue   (b) Back    (m) Menu           "+B+"│")
print(""+B+"│"+G+"                                                "+B+"│")
print(""+B+"└────────────────────────────────────────────────┘")