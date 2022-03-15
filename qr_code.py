# -- imports -- #
import sys
import pyqrcode
from colorama import Fore, Back
from pyqrcode import QRCode
import os


# -- banner -- #
os.system("clear")
banner = Fore.GREEN+f"""

  █████   ██▀███      ▄████▄   ▒█████  ▓█████▄ ▓█████ 
▒██▓  ██▒▓██ ▒ ██▒   ▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ 
▒██▒  ██░▓██ ░▄█ ▒   ▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   
░██  █▀ ░▒██▀▀█▄     ▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄ 
░▒███▒█▄ ░██▓ ▒██▒   ▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒
░░ ▒▒░ ▒ ░ ▒▓ ░▒▓░   ░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░
 ░ ▒░  ░   ░▒ ░ ▒░     ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░
   ░   ░   ░░   ░    ░        ░ ░ ░ ▒   ░ ░  ░    ░   
    ░       ░        ░ ░          ░ ░     ░       ░  ░
                     ░                  ░             
"""
print(banner)

namee = input("Enter image name (.svg) : ")
urrrl = input("Enter url : ")
try:
    print(f" [$] The url has been successfully converted to QR code.. ")
    myQR = QRCode(urrrl)
    print(f" [$] QR Code Saved here >> {namee} ")
    myQR.svg(namee, scale= 8)

except FileNotFoundError:
    os.system("clear") #for linux
    print(banner)
    print(" [X] Url or image name Wrongly spelled")
    exit()