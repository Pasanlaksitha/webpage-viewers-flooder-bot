import webbrowser
import time
import os

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'

timed = int(input("View Time (sec) : "))
url = input("Enter URL: ")
cycles = int(input("Views : "))

for bulk in range(cycles):
    webbrowser.get(chrome_path).open_new(url)
    time.sleep(timed)
    os.system("taskkill /im chrome.exe /f")
os.system("taskkill /im chrome.exe /f")
