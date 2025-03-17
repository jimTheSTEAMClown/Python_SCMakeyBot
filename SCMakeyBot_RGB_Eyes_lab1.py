# SCMakeyBot Robot Control
# ============================================================================
# Source: STEAM Clown - www.steamclown.org 
# GitHub: https://github.com/jimTheSTEAMClown/Python_SCMakeyBot
# GitHub: https://raw.githubusercontent.com/jimTheSTEAMClown/Python_SCMakeyBot/refs/heads/main/SCMakeyBot_RGB_Eyes_lab1.py
# Hacker: Jim Burnham - STEAM Clown, Engineer, Teacher, Maker, Propmaster & Adrenologist  
# This example code is licensed under the CC BY-NC-SA 4.0, GNU GPL and EUPL
# https://creativecommons.org/licenses/by-nc-sa/4.0/
# https://www.gnu.org/licenses/gpl-3.0.en.html
# https://eupl.eu/
# Program/Design Name:        SCMakeyBot.py <-- or a test/template sub version
# Description:    This is a program to control a "RGB Eyes of the SCMaketBot"
# 
# program description:
# 1) Read user input from consol or data file, or web.
# Dependencies:   python3
#   Inputs: <list any expected user input here>
#   Outputs: <list any expected program output here>
# Revision:  
#  Revision 0.01 - Created 03/16/2025
# Additional Comments: 
# 
# ============================================================================
# Raspberry Pi Global Setting
from gpiozero import LED
from gpiozero import PWMLED
import time

# Debug Settings
debug_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if debug_messages : print("Debug Message are 'ON'")
else : print("Debug Message are 'OFF'")

# Raspberry Pi Pins
red_pwm_pin = PWMLED(3) 
green_pwm_pin = PWMLED(4) 
blue_pwm_pin = PWMLED(17) 

def eyes_RGB(eyes_status):
    if debug_messages : print("Running eyes_RGB function")
    if debug_messages : print(eyes_status)
    red,green,blue = eyes_status
    red_pwm_pin.value = eyes_status[red]
    green_pwm_pin.value = eyes_status[green]
    blue_pwm_pin.value = eyes_status[blue]

def main():
    print("Welcome To The STEAM Clown Makey Bot")
    eyes_RGBLEDs = {'red_RGBLED':.1, 'green_RGBLED':.5, 'blue_RGBLED':.99}
    #eyes_RGBLEDs = {'left_eye':{'leye_red_RGBLED':1, 'leye_green_RGBLED':.5, 'leye_blue_RGBLED':.99}, 'right_eye':{'reye_red_RGBLED':1, 'reye_green_RGBLED':.5, 'reye_blue_RGBLED':.99}}
    if debug_messages : print("Calling eyes_RGB function")
    eyes_RGB(eyes_RGBLEDs)
    if debug_messages : print("Returned from eyes_RGB function")

main()
