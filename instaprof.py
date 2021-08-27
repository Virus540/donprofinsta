import instaloader
import time
import os

class color:
	CYAN = '\033[96m'
	RED = '\033[91m'
	YELLOW = '\033[93m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	END = '\033[0m'
time.sleep(1)
print (color.RED +     """
$$$$$$$$$$$$$$$$$$$
$                 $
$                 $
$    virus450     $
$                 $
$                 $
$$$$$$$$$$$$$$$$$$$
""" + color.END)
ig = instaloader.Instaloader()

profiles = str(input(color.YELLOW + "enter username : " + color.END))
os.system('clear')
os.system('clear')
print(color.BLUE + "<⌛>" + color.END)
time.sleep(1)
print(color.BLUE + "[➣➣]" + color.END)
time.sleep(1)
print(color.BLUE + "[➣➣➣➣‌]" + color.END)
time.sleep(1)
print(color.BLUE + "[➣➣➣➣➣➣]" + color.END)
time.sleep(1)
print(color.BLUE + "[➣➣➣➣➣➣➣]" + color.END)
time.sleep(1)
print(color.BLUE + "[➣➣➣➣➣➣➣➣➣]" + color.END)
time.sleep(1)
print(color.GREEN + "---------------------------" + color.END)
time.sleep(2)
os.system('clear')
ig.download_profile(profiles, profile_pic_only = True)
