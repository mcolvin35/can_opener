import time
import digitalio as DIo
from adafruit_motor import stepper,servo
import board
from analogio import AnalogIn, AnalogOut 

btn = DIo.DigitalInOut(board.D5)
btn.direction = DIo.Direction.INPUT
btn.pull = DIo.Pull.DOWN

prevState = 0     
curState = 0  
savedTime =0

def btncall(btnVal):
    global savedTime
    global curState
    global prevState
    
    if btnVal == False and prevState == True:
        print("back")
        pass
        #go back and 
    if btnVal == True:
        savedTime +=.01
        prevState = True

    elif btnVal == False:
        
        prevState = False
        savedTime =0
    print(f"{savedTime} {prevState} {btnVal}")


while True:
    time.sleep(1)
    btncall(btn.value)
    