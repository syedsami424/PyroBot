from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui
from selenium.webdriver.common.keys import Keys
from PIL import Image
import pytesseract
import time
#from selenium.webdriver.common.options import Options

'''driver=webdriver.Chrome('./chromedriver.exe')
url="https://monkeytype.com"
driver.get(url)'''

driver_path="./webdriver/chromedriver"
chromeService=Service(driver_path)

browser=webdriver.Chrome(service=chromeService)

url= "https://10fastfingers.com/typing-test/english"
browser.get(url)
time.sleep(7)

pyautogui.click(x=1271, y=606) #remove ad
pyautogui.click(x=1011, y=876) #allow cookies

for i in range(18):
    time.sleep(1)
    screenshot=pyautogui.screenshot(region=(350,362,943,133))
    screenshot.save('10fastfingers.png')
    image1=Image.open('10fastfingers.png')
    image1=image1.convert("L")#grayscale conversionge1=image1 .convert("L")#grayscale conversion is one
    #this one fucking line SAVED my ASSSSSSSS
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text1=pytesseract.image_to_string(image1)
    print(text1)

    #text="The quick brown fox jumps over the lazy dog"
    pyautogui.PAUSE=0.0
    wordlist=text1.split()
    #wordlist=[i for i in text]

    #words from monkeytype1
    pyautogui.click(x=864, y=542) #click on type box
    for word in wordlist:
        pyautogui.typewrite(word)
        pyautogui.press('space')

#Point(x=60, y=540) top left

#Point(x=1252, y=639) bottom right

#w=1192
#h=99

'''for i in range(19):
    time.sleep(2)
    screenshot=pyautogui.screenshot(region=(60,540,1237,99))
    screenshot.save('monkeytype2.png')
    image2=Image.open('monkeytype2.png')
    image2=image2.convert("L")
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text2=pytesseract.image_to_string(image2)

    pyautogui.PAUSE=0.0 #infinite wpm
    wordlist2=text2.split()
    n=len(wordlist2)
    #first=wordlist2[0]
    #f=first[0]
    #wordlist2=text2[1:]
    print(text2)
    for word in wordlist2:
        pyautogui.typewrite(word)
        pyautogui.PAUSE=0.0 #infinite wpm
        pyautogui.press('space')
'''
    #for below problem, just make it so that it pyautogui takes a very precise screenshot
'''first=wordlist2[0]
    f=first[0]
    if(f=="J" or f=="|"):
        wordlist2=text2[1:]
        for word in wordlist2:
            pyautogui.typewrite(word)
    else:
        for word in wordlist2:
            pyautogui.typewrite(word)
            pyautogui.press('space')'''

    #for the second problem, list slice the first element and write the rest.

'''if(last element of text1 == first element of text2):
        {logic to slice the first element of text2
        and write the rest.}'''

'''time.sleep(1)
screenshot=pyautogui.screenshot(region=(60,540,1237,99))
screenshot.save('monkeytype3.png')
image3=Image.open('monkeytype3.png')
image3=image3.convert("L")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text3=pytesseract.image_to_string(image3)
print(text3)

pyautogui.PAUSE=0.0 #infinite wpm
wordlist3=text3.split()
#wordlist=[i for i in text]

#words from monkeytype2
for word in wordlist3:
    pyautogui.typewrite(word)
    pyautogui.press('space')

time.sleep(1)
screenshot=pyautogui.screenshot(region=(60,540,1237,99))
screenshot.save('monkeytype4.png')
image4=Image.open('monkeytype4.png')
image4=image4.convert("L")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text4=pytesseract.image_to_string(image4)
print(text4)

pyautogui.PAUSE=0.0 #infinite wpm
wordlist4=text4.split()
#wordlist=[i for i in text]

#words from monkeytype2
for word in wordlist4:
    pyautogui.typewrite(word)
    pyautogui.press('space')



'''







'''
#text="The quick brown fox jumps over the lazy dog"
pyautogui.PAUSE=0.0 #infinite wpm
wordlist=text.split()
#wordlist=[i for i in text]
for word in wordlist:
    pyautogui.typewrite(word)
    pyautogui.press('space')'''

'''chrome_driver_path = './chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

url = 'https://www.example.com'
driver.get(url)

driver.quit()'''