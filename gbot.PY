import pyautogui
import time
#function for later use
def spam():
    time.sleep(5)
    times = ['', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '','', '']
    for word in times:
        pyautogui.typewrite("hello there, this is an automated spam bot. It does not focus on annoying you, because it turns on only if you have the 'do not disturb' mode.")
        pyautogui.press("enter")    

#welcome, I mean, cool ascii art

print("   ____ ___.             __    "
  "/ ___\\_ |__    ____ _/  |_  "
 "/ /_/  >| __ \  /  _ \\   __\ "
" \___  / | \_\ \(  <_> )|  |   "
"/_____/  |___  / \____/ |__|   "
"             \/               "
"                              ")
print("Welcome to the spam bot 1.2!")
print("for use in educational puposes")
print("made by gprogramming, follow me on gihub!")

#questionable ethics (if ya know what I mean)
educationalpurposes = input("Are you going to use this tool only in educational purposes? y/n")
if educationalpurposes == "y":
    spam()
elif educationalpurposes == "n":
    print("You were not supposed to be here, dr. Freeman.")
else:
    print("what did you say?")





