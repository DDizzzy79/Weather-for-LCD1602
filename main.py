#!/user/bin/env python 
import smbus
import time
import sys
import LCD1602 as LCD
import weather1 as wea
if __name__ == '__main__':
    temp = wea.RetWea()
    LCD.init_lcd()
    time.sleep(1)
    LCD.turn_light(1)
    LCD.print_lcd(0,0,"It is " + temp + "C" )
    while True:
        nowtime = time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))
        hourtime = time.strftime('%H',time.localtime(time.time()))
        mintime = time.strftime('%M',time.localtime(time.time()))
        sectime = time.strftime('%S',time.localtime(time.time()))
        LCD.print_lcd(1,1,nowtime)
        if mintime == '59':
            if sectime == '00':
                LCD.turn_light(1)
            elif sectime  == '59':
                LCD.turn_light(0)
        time.sleep(0.2)
