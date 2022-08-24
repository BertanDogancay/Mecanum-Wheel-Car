import time
import pygame
from time import sleep
import ps4 as js
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

x=0
movement = 'Joystick'

class Motor1():
    def __init__(self, In1, In2):
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.In1, GPIO.OUT)
        GPIO.setup(self.In2, GPIO.OUT)
    def moveF(self,x):
        GPIO.output(self.In1, GPIO.HIGH)
        GPIO.output(self.In2, GPIO.LOW)
    def moveB(self,x):
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.HIGH)
    def stop(self):
        GPIO.output(self.In1, GPIO.LOW)
        GPIO.output(self.In2, GPIO.LOW)
    
class Motor2():
    def __init__(self, Ena2, In3, In4):
        self.Ena2 = Ena2
        self.In3 = In3
        self.In4 = In4
        GPIO.setup(self.Ena2, GPIO.OUT)
        GPIO.setup(self.In3, GPIO.OUT)
        GPIO.setup(self.In4, GPIO.OUT)
        self.i = GPIO.PWM(self.Ena2, 100)
        self.i.start(0)
    def moveF(self,x):
        GPIO.output(self.In3, GPIO.HIGH)
        GPIO.output(self.In4, GPIO.LOW)
        self.i.ChangeDutyCycle(x)
    def moveB(self,x):
        GPIO.output(self.In3, GPIO.LOW)
        GPIO.output(self.In4, GPIO.HIGH)
        self.i.ChangeDutyCycle(x)
    def speed(self,x):
        self.i.ChangeDutyCycle(x)
         
class Motor3():
    def __init__(self, Ena3, In5, In6):
        self.Ena3 = Ena3
        self.In5 = In5
        self.In6 = In6
        GPIO.setup(self.Ena3, GPIO.OUT)
        GPIO.setup(self.In5, GPIO.OUT)
        GPIO.setup(self.In6, GPIO.OUT)
        self.a = GPIO.PWM(self.Ena3, 100)
        self.a.start(0)
    def moveF(self,x):
        GPIO.output(self.In5, GPIO.HIGH)
        GPIO.output(self.In6, GPIO.LOW)
        self.a.ChangeDutyCycle(x)
    def moveB(self,x):
        GPIO.output(self.In5, GPIO.LOW)
        GPIO.output(self.In6, GPIO.HIGH)
        self.a.ChangeDutyCycle(x)
    def speed(self,x):
        self.a.ChangeDutyCycle(x)
        
class Motor4():
    def __init__(self, Ena4, In7,In8):
        self.Ena4 = Ena4
        self.In7 = In7
        self.In8 = In8
        GPIO.setup(self.Ena4, GPIO.OUT)
        GPIO.setup(self.In7, GPIO.OUT)
        GPIO.setup(self.In8, GPIO.OUT)
        self.j = GPIO.PWM(self.Ena4, 100)
        self.j.start(0)
    def moveF(self,x):
        GPIO.output(self.In7, GPIO.HIGH)
        GPIO.output(self.In8, GPIO.LOW)
        self.j.ChangeDutyCycle(x)
    def moveB(self,x):
        GPIO.output(self.In7, GPIO.LOW)
        GPIO.output(self.In8, GPIO.HIGH)
        self.j.ChangeDutyCycle(x)
    def speed(self,x):
        self.j.ChangeDutyCycle(x)
        
         
motor1 = Motor1(18, 17)
motor2 = Motor1(22, 23)
motor3 = Motor1(9, 25)
motor4 = Motor1(24, 27)


while True:

    pygame.init()
    
    if movement == 'Joystick':
        jsVal = js.getJS()
        
        if jsVal['R2']:
            x = 50
            motor1.moveF(x)
            motor2.moveF(x)
            motor3.moveF(x)
            motor4.moveF(x)
               
        if jsVal['L2']:
            motor1.moveB(x)
            motor2.moveB(x)
            motor3.moveB(x)
            motor4.moveB(x)

        if jsVal['axis1'] or jsVal['axis2']:
            if jsVal['axis1'] > 0:
                motor1.moveB(x)
                motor2.moveF(x)
                motor3.moveF(x)
                motor4.moveB(x)
            elif jsVal['axis1'] < 0:
                motor1.moveF(x)
                motor2.moveB(x)
                motor3.moveB(x)
                motor4.moveF(x)
        
        if jsVal['L1']:
            motor1.moveF(x)
            motor2.moveB(x)
            motor3.moveF(x)
            motor4.moveB(x)


        if jsVal['R1']:
            motor1.stop()
            motor2.stop()
            motor3.stop()
            motor4.stop()