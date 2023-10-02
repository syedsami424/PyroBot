import os
import pyautogui
import time
from PIL import Image
import pytesseract



'''f=open("D:\example_file.txt", "a")
os.startfile(r'D:\example_file.txt')
time.sleep(3)
pyautogui.write('Hello There', interval = 0.1)
pyautogui.press('enter')
pyautogui.write('How is the Weather?', interval = 0.1)
#pyautogui.hotkey('alt', 'f4')
pyautogui.press('enter')'''

'''time.sleep(3)
#create an algorithm to auto detect words in a website
text="The quick brown fox jumps over the lazy dog"
pyautogui.PAUSE=0.0 #infinite wpm
wordlist=text.split()

#wordlist=[i for i in text]
for word in wordlist:
    pyautogui.typewrite(word)
    pyautogui.press('space')'''



'''
#OCR (Optical Character Recognition)
screenshot=pyautogui.screenshot("screenshot.png")
image=Image.open("screenshot.png")
#grayscale conversion
image=image.convert("L")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text=pytesseract.image_to_string(image)
print(text)'''

'''
#screenshot=pyautogui.screenshot(region=(171,480,1200,1250))
pyautogui.screenshot("monkeytype.png")
#img=cv2
screenshot.save('monkeytype1.png')
image=Image.open('monkeytype1.png')
image=image.convert("L")#grayscale conversion
#this one fucking line SAVED my ASSSSSSSSS
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text=pytesseract.image_to_string(image)
print(text)
'''

text2="The only ones who should kill are those prepared to be killed."
pyautogui.PAUSE=0.0 #infinite wpm
wordlist2=text2.split()
n=len(wordlist2)
#first=wordlist2[0]
#f=first[0]
#wordlist2=text2[1:]

'''
first=wordlist2[0]
f=first[0]
if(f=="J" or f=="|"):
    wordlist2=text2[1:]
    for word in wordlist2:
        pyautogui.typewrite(word)
else:
    for word in wordlist2:
        pyautogui.typewrite(word)
        pyautogui.press('space')
'''
#ORRRR, JUST TAKE A VERY VERY PRECISE SCREENSHOT.
tessBaseApi.setVariable(TessBaseAPI.VAR_CHAR_WHITELIST,whiteList);

    #pyautogui.press('space')
        #then backspace it OR list slicing