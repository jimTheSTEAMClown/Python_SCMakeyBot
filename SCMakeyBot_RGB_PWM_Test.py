# SCMakeyBot Robot Control
# ============================================================================
# Source: STEAM Clown - www.steamclown.org 
# GitHub: https://raw.githubusercontent.com/jimTheSTEAMClown/RaspberryPi/master/RPi_NeoPixel_Strip.py
# Hacker: Jim Burnham - STEAM Clown, Engineer, Teacher, Maker, Propmaster & Adrenologist  
# This example code is licensed under the CC BY-NC-SA 4.0, GNU GPL and EUPL
# https://creativecommons.org/licenses/by-nc-sa/4.0/
# https://www.gnu.org/licenses/gpl-3.0.en.html
# https://eupl.eu/
# Program/Design Name:        SCMakeyBot.py
# Description:    This is a program to control an LED (PWM)
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
led_pwm_pin = PWMLED(3) 
 
def led_RGB(brightness):
    if debug_messages : print("Running led_RGB function")
    if debug_messages : print(brightness)
    led_pwm_pin.value = brightness
    
def main():
    print("Welcome To The STEAM Clown Makey Bot")
    while(True):
        user_RGB_value = float(input("Enter a number from 0-1, so 0, .42, .82, or 1 is OK > "))
        if debug_messages : print("Calling led_RGB function")
        led_RGB(user_RGB_value)
        if debug_messages : print("Returned from led_RGB function")

main()
