import pyfiglet
from termcolor import colored
import pyautogui
from time import sleep
from webbrowser import open
import os
os.system("clear")
tweettwitter = pyfiglet.figlet_format("tweet twitter")
print(colored(tweettwitter,'blue'))
msg=input("enter the tweet: ")
num_msg=(1)
time_msg=float(5)
open("https://twitter.com/compose/tweet")
sleep(5)
for num in range(num_msg+1):
    pyautogui.typewrite(msg)
    sleep(time_msg)
    pyautogui.press('enter')
    sleep(time_msg)

