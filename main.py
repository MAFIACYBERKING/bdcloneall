import os
import time
import sys
import random
from threading import Thread as pool

#text colour()

white = '\33[90m'
red = '\33[91m'
green = '\33[92m'
yollow = '\33[93m'
blue = '\33[94m'
rosy = '\33[95m'
pest = '\33[96m'
blue = '\x1b[94m'
lightblue = '\x1b[94m'
red = '\x1b[91m'
white = '\x1b[97m'
green = '\x1b[93m'
green = '\x1b[1;32m'
cyan = '\x1b[96m'
end = '\x1b[0m'
yellow = '\n\n\x1b[1;93m'
#colour end

os.system("clear")
logo11=(yellow+"""
███╗░░░███╗██████╗░
████╗░████║██╔══██╗
██╔████╔██║██║░░██║
██║╚██╔╝██║██║░░██║
██║░╚═╝░██║██████╔╝
╚═╝░░░░░╚═╝╚═════╝░

░█████╗░██╗░░░░░░█████╗░███╗░░░███╗██╗███╗░░██╗
██╔══██╗██║░░░░░██╔══██╗████╗░████║██║████╗░██║
███████║██║░░░░░███████║██╔████╔██║██║██╔██╗██║
██╔══██║██║░░░░░██╔══██║██║╚██╔╝██║██║██║╚████║
██║░░██║███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝



\x1b[94m

╔═══╦╗─╔╦═══╦╗╔╗╔╦═══╦╗─╔╦╗─╔╦═══╦╗──╔╗
║╔═╗║║─║║╔═╗║║║║║╠╗╔╗║║─║║║─║║╔═╗║╚╗╔╝║
║║─╚╣╚═╝║║─║║║║║║║║║║║╚═╝║║─║║╚═╝╠╗╚╝╔╝
║║─╔╣╔═╗║║─║║╚╝╚╝║║║║║╔═╗║║─║║╔╗╔╝╚╗╔╝
║╚═╝║║─║║╚═╝╠╗╔╗╔╬╝╚╝║║─║║╚═╝║║║╚╗─║║
╚═══╩╝─╚╩═══╝╚╝╚╝╚═══╩╝─╚╩═══╩╝╚═╝─╚╝""")


alamin=(green+"\n---------------------- Delovement by MD ALAMIN CHOWDOWRY  --------")



#download package





print(logo11)
print(alamin)
x=3
while x<5:
     user=str(input(red+"\n ?? USERNAME : "))
     passw=str(input(green+"\n ☣️PASSWORD : "))
     if user=="alamin" and passw=="alamin":
      print("Login Succcessfull")
      sys.stdout.flush()
      time.sleep(5) 
      os.system("xdg-open https://www.facebook.com/Mdalamin54321")
      x=8
     else:
      	print(red+"\n\t⚠️username or password incorrect⚠️   ")
      	os.system("xdg-open https://www.facebook.com/Mdalamin54321")
      	x=3
      	
os.system("clear")
print(logo11)
print(alamin)
print("\n\n[1] 6  Digit  Password \n\n[2] 7  Digit  Password \n\n[3] 8 Digit  Password\n\n[4] 9 Digit  Password  \n\n[5] Contact Me")

a=input(blue+"\n\nEnter Your Fovarite Number password: ")

if a=="1":
	os.system("python newfile.py")
if a=="2":
	os.system("python newfile.py2")
if a=="3":
	os.system("python newfile.py3 ")
if a=="4":
	os.system("python newfile.py4")
if a=="5":
	os.system("xdg-open https://www.facebook.com/Mdalamin54321")
      	