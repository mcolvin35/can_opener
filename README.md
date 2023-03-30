# **Can Opener Project!**
## ***Table of Contents***
* [Planning](#Hello-Circuitpython!)
* [Materials](#Servo)
* [Wiring+Code](#ultrasonic-sensor)
* [CAD](#lcd)
* [Final Result](#motor-control)
* [Complications](#complications)

## ***Planning***
### **Description**
Get **Circuitpython** and the **Metroexpress** boards up and running, make the onboard neopixel LED **glow**
### **Evidence** 
```python
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1) #links led to board
dot.brightness=0.5 #sets brightness to half to prevent blindness

print("Make it pink!") #prints "Make it pink!" to the serial monitor 

while True:
    dot.fill((255, 50, 85)) #makes the led pink
```
### **Image**
<img src="https://github.com/mcolvin35/circuit-python/blob/master/images/hello_circuitpy.png?raw=true" width="500">

No wiring necessary for this one, **Metroexpress** boards have an LED built in :)

### **Reflection**
Getting everything set up was overwhelming and complicated, but Mr. H, River, and Josie were super helpful in getting things working. Thanks!


## ***Materials***

## ***Wiring+Code***

## ***CAD***

## ***Final Result!***
