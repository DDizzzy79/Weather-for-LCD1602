#!/user/bin/env python 
import smbus
import time
import sys
import LCD1602 as LCD
import weather as wea
if __name__ == '__main__':
    temp = wea.RetWea()
    weather = "The temperature is",temp,"now"
    LCD.init_lcd()
    time.sleep(1)
    LCD.turn_light(1)
    while True:
        LCD.print_lcd(1, 1, weather)
        time.sleep(0.2)