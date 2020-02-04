#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

#Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
def force_to_unicode(text): 
  "If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding" 
  return text if isinstance(text, unicode) else text.decode('utf8')
 
print
print(""+R+"╭───────────────────╮")
print(""+R+"┃"+G+" 〔 ➊  Continue 〕 "+R+"┃")
print(""+R+"┃"+G+" 〔 ➋  About    〕 "+R+"┃")
print(""+R+"┃"+R+" 〔 ✖  Exit     〕 "+R+"┃")
print(""+R+"╰───────────────────╯")
print