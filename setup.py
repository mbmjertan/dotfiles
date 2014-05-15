#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import operator

print 'Postinstall wizard'
print 'za Ubuntu/Debian'
print 'Za nastavak unesite Y, a za izlaz X'

choice = raw_input()

if choice == "X":
	print 'izlazim'
	exit()
elif choice == "Y":
	print 'ok, nastavljam'
else:
	print 'nevaljan izbor, izlazim'
	exit()

print 'update repozitorija slijedi'

proc = subprocess.Popen('sudo apt-get update -y', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()
if err=='':
	print out
	print 'repozitoriji ažurirani'
else:
	print out
	print err
	print 'greška'

print 'upgrade distribucije slijedi'

proc = subprocess.Popen('sudo apt-get upgrade -y', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()
if err=='':
	print out
	print 'distribucija upgradeana'
else:
	print out
	print err
	print 'greška'

print 'instaliram qbittorrent'

proc = subprocess.Popen('sudo apt-get install qbittorrent -y', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()
if err=='':
	print out
	print 'aplikacija instalirana'
else:
	print out
	print err
	print 'greška'

print 'instaliram vlc'

proc = subprocess.Popen('sudo apt-get install vlc -y', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()
if err=='':
	print out
	print 'aplikacija instalirana'
else:
	print out
	print err
	print 'greška'

print 'instaliram firefox'

proc = subprocess.Popen('sudo apt-get install firefox -y', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()
if err=='':
	print out
	print 'aplikacija instalirana'
else:
	print out
	print err
	print 'greška'

print 'instaliram chromium'

proc = subprocess.Popen('sudo apt-get install chromium -y', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()
if err=='':
	print out
	print 'aplikacija instalirana'
else:
	print out
	print err
	print 'greška'

print 'instaliram libreoffice'

proc = subprocess.Popen('sudo apt-get install libreoffice -y', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()
if err=='':
	print out
	print 'aplikacija instalirana'
else:
	print out
	print err
	print 'greška'

print 'instaliram pidgin'

proc = subprocess.Popen('sudo apt-get install pidgin -y', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()
if err=='':
	print out
	print 'aplikacija instalirana'
else:
	print out
	print err
	print 'greška'

print 'instaliram gimp'

proc = subprocess.Popen('sudo apt-get install gimp -y', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()
if err=='':
	print out
	print 'aplikacija instalirana'
else:
	print out
	print err
	print 'greška'

print 'instaliram geogebra'

proc = subprocess.Popen('sudo apt-get install geogebra -y', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()
if err=='':
	print out
	print 'aplikacija instalirana'
else:
	print out
	print err
	print 'greška'

print 'instaliram smplayer'

proc = subprocess.Popen('sudo apt-get install smplayer -y', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()
if err=='':
	print out
	print 'aplikacija instalirana'
else:
	print out
	print err
	print 'greška'

print 'instaliram gparted'

proc = subprocess.Popen('sudo apt-get install gparted -y', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()
if err=='':
	print out
	print 'aplikacija instalirana'
else:
	print out
	print err
	print 'greška'

print 'POSTINSTALL ZAVRŠEN'
print 'kraj programa'
