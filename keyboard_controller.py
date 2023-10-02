'''             initial plans:-            '''
#ethical hacking program that opens a text file in someone else's laptop and types something
#ethical hacking program that shuts down a user's laptop by accessing hotkeys

import os
import pyautogui

import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from PIL import Image
import pytesseract

from datetime import date
########################################
'''    THIS ONLY TYPES STUFF IN PYTHON

from pynput.keyboard import Key, Controller
keyboard = Controller()
keyboard.type('Hello World')
keyboard.press(Key.space)
keyboard.release(Key.space)

with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')'''
#########################################
'''THIS TYPES STUFF ONTO THE FILE'''

#you could also create a mini chat bot that answers your questions.
#ORRRR, create a menu and from that menu, the chat bot responds.


#to read user input:-
'''logic here is, the above function's input will be the last line, which will be our query.
Sooo..traverse through the last line and find a specific keyword and pyautogui.write("answer")'''

'''or, why do with something complicated like above. why not just use toFile?'''

'''                     Maybe play a song           '''


'''f1=open("D:\example_file.txt", "r")
print("here")
for line in f1:
    pass
last_line=line
print(last_line)'''
'''last_line=f1.readlines()[-1]
print(last_line)'''

#################################################
from datetime import date
'''def date():
    #global flag
    #if(flag==1):
    Today=date.today()
    d1=Today.strftime("%d/%m/%Y")
    pyautogui.press('enter')
    pyautogui.write("Today's date is: "+d1, interval=0.1)
    print("d1 =", d1)
    d2 = Today.strftime("%B %d, %Y")
    pyautogui.press('enter')
    pyautogui.write(d2, interval=0.1)
    print("d2 =", d2)'''

##########################################
#to take user input(query):-
def query():
    global user_name1
    pyautogui.press('enter')
    pyautogui.write(user_name1+": What is your query?", interval=0.1)
    pyautogui.press('enter')
    user_query=pyautogui.prompt("Write what you want into the field: ") #observation: if you dont type pyautogui.prompt("dlfds") and instead go like toFile=input("Enter query"), it will print it in the console.
    #time.sleep(3)
    f.write(user_query)
    pyautogui.write(user_query, interval=0.1)

    ################ QUERY CHECKER ###################
    print(user_query)
    temp_query=user_query.split()
    L=len(temp_query)
    flag=0
    for i in range(L):
        print(temp_query[i].lower())
        if(temp_query[i].lower()=='date'):
            print("found at ",i)
            keyword=temp_query[i]
            flag=1
            break
    ################# DATE ###################
    if(flag==1):
        Today=date.today()
        d1=Today.strftime("%d/%m/%Y")
        pyautogui.press('enter')
        pyautogui.write("Today's date is: "+d1, interval=0.1)
        print("d1 =", d1)
        d2 = Today.strftime("%B %d, %Y")
        pyautogui.press('enter')
        pyautogui.write(d2, interval=0.1)
        print("d2 =", d2)
###########################################
'''              MONKEY TYPE             '''
def monkey_type():
        pyautogui.press('enter')
        pyautogui.write("Opening monkeytype...",interval=0.1)
        time.sleep(2)
        #opening monkeytype
        driver_path="./webdriver/chromedriver"
        chromeService=Service(driver_path)
        browser=webdriver.Chrome(service=chromeService)
        url= "https://monkeytype.com/"
        browser.get(url)
        time.sleep(5)

        '''     OCR (Optical Character Recognition)     '''

        #use cv2 library for cropping image to whatever ratio you want
        #code to run below lines only when a click is detected.

        screenshot=pyautogui.screenshot(region=(171,480,1200,25))
        screenshot.save('monkeytype.png')
        image=Image.open('monkeytype.png')
        image=image.convert("L")#grayscale conversion
        #this one fucking line SAVED my ASSSSSSSSS
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text=pytesseract.image_to_string(image)
        print(text)

        #text="The quick brown fox jumps over the lazy dog"
        pyautogui.PAUSE=0.0 #infinite wpm
        wordlist=text.split()
        #wordlist=[i for i in text]
        for word in wordlist:
            pyautogui.typewrite(word)
            pyautogui.press('space')



###########################################
'''              PLAY A SONG            '''


###########################################
'''           MORE BASIC FUNCTIONS      '''


###########################################
'''             TELL ME A JOKE          '''


###########################################
'''         STEVE DINOSAUR JUMP GAME    '''


###########################################
'''               MENU              '''
def main_menu():
    global user_name1
    while True:
        print("in main menu function")
        pyautogui.press('\t')
        pyautogui.write("=====================================")
        pyautogui.press('enter')
        pyautogui.write("Enter a choice from the following:-", interval=0.1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.write("1. Enter a query.",interval=0.1)
        pyautogui.press('enter')
        pyautogui.write("2. Exit.",interval=0.1)
        pyautogui.press('enter')
        ''' create a function that will help you in a tying game like monkey type '''
        choice=pyautogui.prompt("Enter choice")

        if(choice=='1'):
            query()
            pyautogui.press('enter')
            pyautogui.write(user_name1+": Would you like to ask another query?",interval=0.1)
            another=pyautogui.prompt("Enter yes/no")
            f.write(another)
            pyautogui.write(another, interval=0.1)

            if(another.lower()=="yes" or another.lower()=="y"):
                query_count=1
                query()
            elif(another.lower()=="no" or another.lower()=="n"):
                pyautogui.press('enter')
                pyautogui.write("Returning to menu",interval=0.1)
                main_menu()

        if(choice=='2'):
            pyautogui.press('enter')
            pyautogui.write("Would you like to save this file?",interval=0.1)
            exit_query=pyautogui.prompt("Save or dont save")

            #literally no point of this
            if(exit_query=='save' or exit_query=='yes' or exit_query=='y'):
                pyautogui.write("exiting...",interval=0.1)
                pyautogui.hotkey('alt','f4')
                pyautogui.press('enter')
                sys.exit()
                print("program terminated")

            elif(exit_query=='dont save' or exit_query=='no' or exit_query=='n' or exit_query=='nope'):
                pyautogui.write("exiting...",interval=0.1)
                pyautogui.hotkey('alt','f4')
                pyautogui.press('right')
                pyautogui.press('enter')
                sys.exit()
                print("program terminated")

        else:
            print("faggot")
            pyautogui.write("faggot",interval=0.1)

f=open("D:\example_file.txt", "w")
os.startfile(r'D:\example_file.txt') #observation: without this, no file opens and everything will get printed onto python console
time.sleep(3)   #observation: without this statement, the program prints everything below in the console instead of the text file.
pyautogui.write("Please pick a name for me.",interval=0.1)
time.sleep(1)
user_name1=pyautogui.prompt("Enter chat user name")
pyautogui.press('enter')
f.write(user_name1)
pyautogui.write(user_name1)
pyautogui.press('enter')
pyautogui.write("Hello there, I am "+user_name1+". You are?",interval=0.1)
time.sleep(1)
pyautogui.press('enter')
user_name=pyautogui.prompt("Enter your name below:-")
f.write(user_name)
pyautogui.write(user_name)
pyautogui.press('enter')
if(user_name==user_name1):
    pyautogui.write("lmao that is my name too, sup nigga", interval=0.1)
    pyautogui.press('enter')

else:
    pyautogui.write(user_name1+": Hi, "+user_name+"!!")
    pyautogui.press('enter')
    time.sleep(1)

main_menu()



###########################################
'''INSTEAD OF ENTIRE SEPARATE FUNCTIONS, JUST MAKEA FUNCT. CALLED QUERY_CHECK, THAT FIND OUT THE KEYWORD IN THE QUERY AND REDIRECT YOU TO THE RESPECTIVE FUNCTION'''
'''             DATE
print(user_query)
temp_query=user_query.split()
L=len(temp_query)
flag=0
for i in range(L):
    print(temp_query[i].lower())
    if(temp_query[i].lower()=='date'):
        print("found at ",i)
        keyword=temp_query[i]
        flag=1
        break
    if(flag==1):
    today=date.today()
    d1=today.strftime("%d/%m/%Y")
    pyautogui.press('enter')
    pyautogui.write("Today's date is: "+d1, interval=0.1)
    print("d1 =", d1)
    d2 = today.strftime("%B %d, %Y")
    pyautogui.press('enter')
    pyautogui.write(d2, interval=0.1)
    print("d2 =", d2)'''

'''else:
        pyautogui.press('enter')
        pyautogui.write(user_name1+": please ensure there aren't any typos in your query.",interval=0.1)
        print("no date keyword found")'''
##############################################

#option to exit with or without saving

print("working")