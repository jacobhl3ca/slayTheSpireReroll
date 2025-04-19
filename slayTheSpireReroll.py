import pyautogui # https://pyautogui.readthedocs.io/en/latest/quickstart.html
pyautogui.FAILSAFE = True
import time
import logging
import os

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