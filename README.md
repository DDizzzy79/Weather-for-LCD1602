# LCD1602HeWeatherPull
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
