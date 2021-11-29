
# ![](https://img.shields.io/badge/Rasp-3B%2B-blueviolet)  ![](https://img.shields.io/badge/python-2.7-blue) ![](https://img.shields.io/badge/-linux-blue) Weather for LCD1602
![a84c29c7402d0e98d61d1eafaf8e504](https://user-images.githubusercontent.com/72267897/143870181-1b8a27c8-cef2-42ea-9546-cc2ae6f0b678.jpg)

* Simple Weather Check base on Hefeng api, Work on raspberry Pi
* 简单基于和风天气的查询 可以被树莓派使用
# How To Use?
Use `git clone https://github.com/DDizzzy79/LCD1602HeWeatherPull.git` Then `cd LCD1602HeWeatherPull` 
Then Use  
```
pi@raspberrypi:~ $ sudo apt-get install i2c-tools   
pi@raspberrypi:~ $ sudo apt-get install python-smbus   
pi@raspberrypi:~ $ sudo i2cdetect -y 1 
```
TO find your i2c Ports, Ater that, config The `LCD1602.py` File , Change The i2c setting to the one you found
Also, In order to set the ports of i2c between RaspberryPi , Use `gpio readall` to check

![image](https://user-images.githubusercontent.com/72267897/143859978-d1a43a35-c8fa-403b-99c4-8bff2853a95b.png)

GND --- GND
VCC --- 5V
SDA --- SDA
SCL --- SCL
