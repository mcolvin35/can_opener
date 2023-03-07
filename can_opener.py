import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo


pwm = pwmio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency= 100)
my_servo = servo = servo.ContinuousServo(pwm, min_pulse=500, max_pulse=2600)
btn = DigitalInOut(board.D12) #links button 1 to board
btn.direction = Direction.INPUT #btn1 is input
btn.pull = Pull.DOWN #recognize input when button is pressed


prev_state = btn.value #previous state is btn1
while True:
    cur_state = btn.value #current state is btn1
    if cur_state != prev_state: #if cur_state is different than prev_state
        if not cur_state:
            print("BTN1 is up")
                 myservo.throttle = -1.0
        else:
            print("BTN1 is down")
                 my_servo.throttle = 1.0 #servo moves 180 degrees in one direction

prev_state = cur_state #sets prev_state to cur_state