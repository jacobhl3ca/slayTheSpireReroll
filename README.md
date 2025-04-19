# Slay the Spire Map Reroll Automation 🃏

A Python script to automatically reroll Slay the Spire map paths until you get a desirable layout. Perfect for strategic players who want to optimize their runs!

![Slay the Spire Screenshot](https://steamcdn-a.akamaihd.net/steam/apps/646570/header.jpg)

## Features ✨
- **Auto-Reroll Maps**: Restarts runs to generate new layouts automatically
- **MacBook Optimized**: Configured for 14" MacBooks with BetterDisplay settings
- **Visual Feedback**: Saves map screenshots for quick evaluation
- **Customizable Delays**: Adjust timings for different hardware setups

## Prerequisites 🛠️
- 14" MacBook (M1/M2 recommended)
- [BetterDisplay](https://betterdisplay.pro/) set to **1800x1169 resolution**
- Slay the Spire running in **Windowed Mode (1792x1120)**
- Python 3.6+ and `pip` installed

## Installation 📦
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/slay-the-spire-reroll.git
   cd slay-the-spire-reroll
Install dependencies:
    ```bash
    pip install pyautogui pillow

## Usage 🚀
1. Launch Slay the Spire and select your character
2. Run the script:
    ```bash
    python reroll_script.py
3. Follow prompts:
Press n to reroll the map
Press y to keep the current layout

## Configuration ⚙️
**Game Setup**
- Resolution: 1800x1169 via BetterDisplay
- Windowed Mode: Set game resolution to 1792x1120

**Script Variables**
- Resolution: 1800x1169 via BetterDisplay
- Windowed Mode: Set game resolution to 1792x1120





Edit these in reroll_script.py:
  ```python
  DELAY_AFTER_CLICK = 0.5  # Adjust for slower/faster PCs
  CHARACTER_POSITION = (x, y)  # Coordinates of your character
  SCREENSHOT_PATH = "current_map.png"  # Map preview save location

## Workflow 🔄

Clicks "Play" for your selected character
Opens map with M key
Captures and displays map
Waits for user input (y/n)
Restarts run or continues based on input
Troubleshooting 🚨


## Disclaimer ⚠️

Use at your own risk. Not affiliated with MegaCrit. May violate platform-specific TOS.

May your paths be full of campfires! 🔥🏹
Star the repo if this helps your Spire runs! ⭐






























