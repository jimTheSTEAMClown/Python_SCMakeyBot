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
# Description:    This is a program to show the function calles of the SCMaketBot"
#
# program description:
# 1) Read user input from consol or data file, or web.
# Dependencies:   python3
#   Inputs: <list any expected user input here>
#   Outputs: <list any expected program output here>
# Revision:  
#  Revision 0.01 - Created 03/19/2025
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

warning_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if warning_messages : print("Warning Message are 'ON'")
else : print("Warning Message are 'OFF'")
# Raspberry Pi Pins
r_red_pwm_pin = PWMLED(14)
r_green_pwm_pin = PWMLED(15)
r_blue_pwm_pin = PWMLED(18)

l_red_pwm_pin = PWMLED(27)
l_green_pwm_pin = PWMLED(22)
l_blue_pwm_pin = PWMLED(23)

red_led = LED(3)
yellow_led = LED(4)
green_led = LED(17)

#print(dir(r_red_pwm_pin))

def stop_light(traffic):
    if debug_messages : print("Running stop_light function")
    if debug_messages : print(traffic)
    red,yellow,green = traffic
    if debug_messages : print(traffic[red])

def eyes_RGB(eyes):
    if debug_messages : print("Running eyes_RGB function")
    if debug_messages : print(eyes)
       
    left_eye, right_eye = eyes
    if debug_messages : print(left_eye)
    if debug_messages : print(right_eye)
   
def get_robot_feature_data():
    if debug_messages : print("Runninng get_robot_feature_data function")
    right_eye = {'leye_red_RGBLED':.44, 'leye_green_RGBLED':.5, 'leye_blue_RGBLED':.99}
    left_eye =  {'reye_red_RGBLED':1, 'reye_green_RGBLED':.5, 'reye_blue_RGBLED':.99}
    stop_light = {'red_LED':1, 'yellow_LED':0, 'green_LED':0}
    # servo
    rfd = [stop_light, left_eye, right_eye]
    if debug_messages : print(rfd)
    if debug_messages : print("Returning get_robot_feature_data function")
    return(rfd)

def main():
    print("Welcome To The STEAM Clown Makey Bot")
    if debug_messages : print("Calling get_robot_feature_data function")
#    robot_features = get_robot_feature_data()
    stop_light_LEDs, left_RGB, right_RGB = get_robot_feature_data()
    if debug_messages : print(stop_light_LEDs)
    if debug_messages : print(left_RGB)
    if debug_messages : print(right_RGB)

    if debug_messages : print("Calling stop_light function")
    stop_light(stop_light_LEDs)
    if debug_messages : print("Returned from stop_light function")

    if debug_messages : print("Calling eyes_RGB function")
    eyes_RGB([left_RGB,right_RGB])
    if debug_messages : print("Returned from eyes_RGB function")

main()
