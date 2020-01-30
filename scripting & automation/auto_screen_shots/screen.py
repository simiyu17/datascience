# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:20:59 2020

@author: simiyu
"""

import pyautogui
from datetime import datetime, date
import time


# define a method that will call whenever button will be clicked
def take_short(file_name):
    screenshot = pyautogui.screenshot()
    screenshot.save(file_name)


def main():
    while True:
        now = datetime.now()
        today = date.today()
        current_time = now.strftime("%H%M%S")
        current_date = today.strftime("%d%m%Y")
        filename = 'shots/'+current_date+'_'+current_time+'.png'
        take_short(filename)
        time.sleep(20)  # sleep for 60 seconds


if __name__ == '__main__':
    main()


