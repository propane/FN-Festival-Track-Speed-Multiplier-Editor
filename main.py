
# Fortnite Track Speed Multiplier Changer
#
# @author Klye

import PySimpleGUI as sg
import win32con, win32api, os

# Path to Fortnite config file
LOCAL_APP_DATA = os.environ['LOCALAPPDATA']
FORTNITEGAME_FILEPATH = LOCAL_APP_DATA + '\\FortniteGame\\Saved\\Config\\WindowsClient'
GAMEUSERSETTINGS_FILENAME = 'GameUserSettings.ini'
FULL_FILE_PATH = FORTNITEGAME_FILEPATH + '\\' + GAMEUSERSETTINGS_FILENAME

#
#  Sets the TrackSpeedMultiplier var in Fortnite config file to desired setting
#     and sets the file to read only so the game does not overwrite this
#
def set_multiplier(speed):
    # set file attributes to normal
    win32api.SetFileAttributes(FULL_FILE_PATH, win32con.FILE_ATTRIBUTE_NORMAL)
    
    line_index = 0
    with open(FULL_FILE_PATH, 'r') as reader: # open the file
        FULL_CFG_FILE_CONTENTS = reader.readlines()

        for line in FULL_CFG_FILE_CONTENTS:
            # scan line content for vars
            line_content = line.split('=')

            # if the line is a variable
            if len(line_content) == 2:
                var_name = line_content[0]
                var_value = line_content[1]

                # set the TrackSpeedMultiplier config var
                if var_name == "TrackSpeedMultiplier":
                    FULL_CFG_FILE_CONTENTS[line_index] = var_name + '=' + str(speed) + '\r'

            line_index += 1 # increment line count

    # write new config content
    with open(FULL_FILE_PATH, mode='w') as writer:
        writer.writelines(FULL_CFG_FILE_CONTENTS)

    # make the file read only
    win32api.SetFileAttributes(FULL_FILE_PATH, win32con.FILE_ATTRIBUTE_READONLY)


def get_key(val, values):
    for key, value in values.items():
        if val == key:
            return value
    return "null"

layout = [
    [sg.Slider(
                (0.05, 5.00),
                1.00,
                0.05,
                orientation="h",
                size=(30, 15),
                key="multiplier_slider",
            )],
    [sg.Button("Apply and close")]
]

# Create the window
window = sg.Window("Fortnite Track Speed Multiplier Changer", layout)

# Create an event loop
while True:
    event, values = window.read()

    multiplier_slider_val = get_key("multiplier_slider", values)

    if event == "Apply and close":
        set_multiplier(multiplier_slider_val)
        sg.popup_ok_cancel("Set multiplier speed to " + str(multiplier_slider_val), title="Saved settings")
        sg.popup("Please restart your game if it is running for settings to apply")

    if event == "Apply and close" or event == sg.WIN_CLOSED:
        break

window.close()