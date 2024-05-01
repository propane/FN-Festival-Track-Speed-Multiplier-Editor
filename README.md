# Fortnite Festival Track-Speed Multiplier Editor

Allows setting other track speed multiplier values for Fortnite's Festival gamemode that are outside the range in the game settings menu.

## What's this do?

Setting the track speed does not change the BPM / pacing of the song and all notes will be played at the same time regardless, this is simply a visual adjustment as to how fast notes will appear on your screen.<br><br>
Choosing a speed below 1.0 in my opinion does not make the game easier and you will end up with a ton of notes appearing at once scrolling very slowly down your screen that you have to hit extremely quickly, since you are essentially compacting the entire song into a couple seconds if you put the multiplier to a very low value.

## Building

### Prerequisites

* **Python3 and PIP** are installed.
* **PyInstaller** package installed. `pip install pyinstaller`
* Required packages installed from **requirements.txt**. `pip install -r requirements.txt` or execute **run.bat**

### From source

Open a command prompt.
CD to working directory.
Run:

    pyinstaller main.py --onefile --windowed

After following these steps you should see a **main.exe** inside a **/dist** directory.
