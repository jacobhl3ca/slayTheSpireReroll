import pyautogui # https://pyautogui.readthedocs.io/en/latest/quickstart.html
pyautogui.FAILSAFE = True
import time
import logging
import os
    
# CONFIGURATION:
# need macbook 14"
# betterdisplay app, set to 1800x1169
# open slay the spire from steam
# see if you like the path/maps you got, otherwise, run this code to re-roll the path/map

# Function to perform the automation
def automate_clicks():

    # Switch to the desired application using AppleScript
    os.system("osascript -e 'tell application \"System Events\" to key code 48 using {command down}'")
    time.sleep(0.1)  # Small delay to ensure the app switch completes

    # Coordinates for abandon sequence
    abandon_positions = [
        (1468, 212),
        (1081, 414),
        (686, 785),
        (742, 1011),
        (763, 1069)
    ]

    # Coordinates for reroll sequence
    reroll_positions = [
        (134, 882),
        (414, 776),
        (818, 998),
        (1388, 1035)
    ]

    # Execute abandon sequence
    for position in abandon_positions:
        pyautogui.moveTo(position[0], position[1], duration=0.2)
        pyautogui.click()
        time.sleep(0.1)

    time.sleep(2.1)  # Delay after abandon sequence

    # Execute reroll sequence
    for position in reroll_positions:
        pyautogui.moveTo(position[0], position[1], duration=0.2)
        pyautogui.click()
        time.sleep(0.2)

    # Final action
    time.sleep(1.3)
    pyautogui.click(631, 1026)
    
    # second click for QA purposes
    # time.sleep(0.2)
    # pyautogui.click()

    # pyautogui.click(467, 1022)

# Run the automation
automate_clicks()



# Final waiting and click after reroll
# time.sleep(1.2)
# pyautogui.click(304, 82) # how to get last position? if last, wait 1.2 seconds, then (304, 82)


# os.system("osascript -e 'tell application \"System Events\" to key code 48 using {command down}'")



# The position is: Point(x=231, y=756)
# Size(width=1512, height=982)

# make script to clean the below -- use anon info here instead of the directories 
# jacob@Jacobs-MacBook-Pro ~ % /usr/bin/python3 /Users/jacob/Documents/GitHub/balatro/balatroAuto.py
# The position is: Point(x=414, y=776)
# Size(width=1800, height=1169)
# jacob@Jacobs-MacBook-Pro ~ % /usr/bin/python3 /Users/jacob/Documents/GitHub/balatro/balatroAuto.py
# The position is: Point(x=818, y=998)
# Size(width=1800, height=1169)
# jacob@Jacobs-MacBook-Pro ~ % /usr/bin/python3 /Users/jacob/Documents/GitHub/balatro/balatroAuto.py
# The position is: Point(x=1388, y=1035)
# Size(width=1800, height=1169)
# jacob@Jacobs-MacBook-Pro ~ % /usr/bin/python3 /Users/jacob/Documents/GitHub/balatro/balatroAuto.py
# The position is: Point(x=467, y=1022)
# Size(width=1800, height=1169)
# jacob@Jacobs-MacBook-Pro ~ % 





# Press the escape key
# pyautogui.press('escape')