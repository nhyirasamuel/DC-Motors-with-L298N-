from machine import Pin, PWM  # Importing PIN and PWM
import time  # Importing time

# OUT1 and OUT2 for Motor A
In1 = Pin(15, Pin.OUT)  # IN1
In2 = Pin(14, Pin.OUT)  # IN2

# OUT3 and OUT4 for Motor B
In3 = Pin(12, Pin.OUT)  # IN3
In4 = Pin(11, Pin.OUT)  # IN4

EN_A = PWM(Pin(13))
EN_B = PWM(Pin(10))

# Defining frequency for enable pins
EN_A.freq(1500)
EN_B.freq(1500)

# Setting maximum duty cycle for maximum speed (0 to 65025)
EN_A.duty_u16(65025)
EN_B.duty_u16(65025)

LED = Pin(21, Pin.OUT)

# Move motors in opposite directions
def move_opposite():
    In1.high()
    In2.low()
    In3.low()
    In4.high()
    LED.low()
     

# Stop
def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()
    LED.high()  
    

while True:
    move_opposite()  # Motors move in opposite directions
    time.sleep(2)
    stop()
    time.sleep(1)
   