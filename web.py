import os
import webbrowser
import random
from time import sleep

logo = f'''
          ||            ||
          ||            ||
          ||            ||
          ||      /\    ||
          ||     /  \   ||
          ||    /    \  ||
          ||  /       \ ||
          ||/          \|| E B R O W S E R
         
 |||||||||||||||CODED BY TIMMY|||||||||
'''


def first():
    search = input("||||||||what do you want to search for>>")
    url = 'https://www.google.com/{search}
    print("searching.....")
    time.sleep(0.2)
    print("gotten ip address ")
    webbrowser.open(url)

print(logo)
first() 

