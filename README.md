# **Can Opener Project!**
## ***Table of Contents***
* [Planning](#planning)
* [Materials](#materials)
* [Wiring+Code](#wiringcode)
* [CAD](#cad)
* [Final Result](#final-result)
* [Complications](#complications)

## ***Planning***
For this project, we decided to make a machine that opens a soda can at the press of a button. We had many different ideas for how to get the can open, and we eventually settled on a sort of pulley system using a servo as a winch. 

<img src="https://github.com/mcolvin35/can_opener/blob/master/images/sketch.png?raw=true" width="500">

*Original sketch that eventually evolved into the pulley idea*

<img src="https://github.com/mcolvin35/can_opener/blob/master/images/pulley_sketch.png?raw=true" width="100"> 

*A compound pulley system that was scrapped for time*



## ***Materials***
* 3D printed parts
* Laser cut parts
* Continuous rotation servo
* Metroexpress board + prototyping shield
* Battery Pack + 6 AA batteries
* Lots of 4-40 screws & nuts
* Paracord
* Switch
* 220 ohm resistor 
* Wires
* Fish hook
* Random metal scrap found in the lab

## **Wiring+Code**
### **Code**
```python
import time
import digitalio as DIo
import pwmio
import servo
import board
from analogio import AnalogIn, AnalogOut 
import pwmio

btn = DIo.DigitalInOut(board.D12)
btn.direction = DIo.Direction.INPUT
btn.pull = DIo.Pull.DOWN

pwm = pwmio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency= 100)
my_servo = servo.ContinuousServo(pwm, min_pulse=500, max_pulse=2600)
my_servo.throttle = 0
prevState = 0     
curState = 0  
savedTime =0

def btncall(btnVal):
    global savedTime
    global curState
    global prevState
    
    if btnVal == False and prevState == True:
        print("back")
        my_servo.throttle = -1
        time.sleep(savedTime)
        savedTime = 0
        #go back 
    if btnVal == True:
        savedTime +=.01
        prevState = True
        if savedTime != 0:
            my_servo.throttle = 1
    elif btnVal == False:
        my_servo.throttle = 0
        print("off")
        prevState = False
    print(f"{savedTime} {prevState} {btnVal}")


while True:
    time.sleep(.01)
    btncall(btn.value)

#by Paul Weder
```

*Huuuge thanks to Paul Weder for writing this code!*

### **Wiring**

<img src="https://github.com/mcolvin35/can_opener/blob/master/images/sodacan_wiring.png?raw=true" width="500"> 


## ***CAD***

<img src="https://github.com/mcolvin35/can_opener/blob/master/images/cad_full.png?raw=true" width="500"> 

*Final CAD assembly*

<img src="https://github.com/mcolvin35/can_opener/blob/master/images/cad_back.png?raw=true" width="500"> 

*Back of the assembly*

*Onshape Link: https://cvilleschools.onshape.com/documents/9c60738ac539389040c0dc06/w/e43589603c3912a4e30a3fab/e/abae56153c7f4831e9b199e3?renderMode=0&uiState=646521db1972396f1b219538*


## ***Final Result***

<img src="https://github.com/mcolvin35/can_opener/blob/master/images/final.gif?raw=true" width="500"> 

*It works! ...kinda*

## ***Complications***

### **Cans**

Did you notice the giant metal bar in the gif that wasn't in the sketches or CAD at all? Yeah, that's because soda cans are actually *way* harder to open than anybody would've guessed. The bar was a last-minute addition to squeeze some extra power into the system. 

### **3/21/23 - The Servo Incident**

At one point, when I turned on the machine, I noticed a really weird smell and saw smoke coming out of a hole in the servo. The servo was fried and I had to take apart the whole thing to replace it. 

<img src="https://github.com/mcolvin35/can_opener/blob/master/images/servo_incident_marked.png?raw=true" width="500"> 

The reason it fried was because of that plastic thing circled in blue at the bottom. Apparently, it was supposed to be inside the servo in order to keep the wires from crossing over each other. So when I turned it on, the wires cooked each other and I had to waste a whole block period replacing the servo. Lesson learned I guess. 

### **Securing the can**
 It wasn't a huge problem or anything but if we were to do this project again I would make sure to have some sort of harness to secure the can, which was something I somehow overlooked during the entire design process. That's why I was holding the can down in the video, otherwise it would just be lifted up. 

## **And that's it!**