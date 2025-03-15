# SCMakeyBot Robot Control
# Raspberry Pi Global Setting
from gpiozero import LED
import time

# Raspberry Pi Pins
# Using BCM GPIO3 I/O on BOARD pin 5
red_led = LED(3) # BCM GPIO3 = BOARD 5
yellow_led = LED(4) # BCM GPIO3 = BOARD 5
green_led = LED(17) # BCM GPIO3 = BOARD 5

def stop_light(traffic_status):
    print(traffic_status)
    red,yellow,green = traffic_status
    print(traffic_status[red])
    if(traffic_status[red]):
        red_led.on()
    else :
        red_led.off()
    if(traffic_status[yellow]):
        yellow_led.on()
    else :
        yellow_led.off()
    if(traffic_status[green]):
        green_led.on()
    else :
        green_led.off()
   
def get_user_stop_light(bits):
        # Get User Data in the form of a 0-7 decimal number
        # or a 010 type binary number. Check the number.
        print(bits)
        stop_bin = input("Enter a binary number for the Stop Light LEDs > ")
        print(stop_bin)
        stop_bin_check = int(stop_bin)
        if (stop_bin_check > -1) and (stop_bin_check < 8):
            print("probably a decimal number between 0-7. Converting to binary")
            stop_bin = bin(stop_bin_check)
            print(stop_bin)
            if stop_bin[2] == "1":
                bits['red_LED'] = 1
            else :
               bits['red_LED'] = 0
            if stop_bin[3] == "1":
                bits['yellow_LED'] = 1
            else :
               bits['yellow_LED'] = 0
            if stop_bin[4] == "1":
                bits['green_LED'] = 1
            else :
               bits['green_LED'] = 0
            print(bits)
           
           
               
        elif (stop_bin_check < 112):
            print("probably a binary number. Converting string to binary")
        return bits  
   

def main():
    print("Welcome To The STEAM Clown Makey Bot")
    traffic_light = {'red_LED':1, 'yellow_LED':0, 'green_LED':0}
    traffic_light = get_user_stop_light(traffic_light)
    stop_light(traffic_light)

main()
