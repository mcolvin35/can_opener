import time
import digitalio as DIo
from adafruit_motor import stepper,servo
import board
from analogio import AnalogIn, AnalogOut 

btn = DIo.DigitalInOut(board.D5)
btn.direction = DIo.Direction.INPUT
btn.pull = DIo.Pull.DOWN

pwm = pwmio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency= 100)
my_servo = servo.ContinuousServo(pwm, min_pulse=500, max_pulse=2600)

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
        prevState = False
    print(f"{savedTime} {prevState} {btnVal}")


while True:
    time.sleep(1)
    btncall(btn.value)
    