#Imports
from adafruit_circuitplayground.express import cpx
from adafruit_hcsr04 import HCSR04
import board
import math
import time
import digitalio
from time import sleep


#Assigning variables 
sonar = HCSR04(trigger_pin = board.A7, echo_pin = board.A6)
ledLeft = digitalio.DigitalInOut(board.A1)
ledLeft.direction = digitalio.Direction.OUTPUT
ledRight = digitalio.DigitalInOut(board.A3)
ledRight.direction = digitalio.Direction.OUTPUT
cpx.pixels.brightness = 0.3

#Indefinite loop
while True:
    try:
        
        #Retrieving values from accelerometer
        x_float, y_float, z_float = cpx.acceleration
            
        #If the board flexes left, then turn on left LED
        if(x_float < -.5):
            ledLeft.value = True
            ledRight.value = False
            
        #If the board flexes right, then turn on right LED
        if(x_float > 0.5):
            ledLeft.value = False
            ledRight.value = True

        #If we detect an object ahead, play warning sound.
        #Making sure the warning sound doesnt go off while dipping nose for night lights
        if(sonar.distance < 15 and y_float < 1.5):
            cpx.play_file("RobloxOof.wav")

        #Raise the board to turn on the lights
        if(y_float < -2.0):
            for i in range(10):
                cpx.pixels[i] = (0,255,255)
                cpx.pixels.show()

        #Push down the board to turn lights off
        if(y_float > 2.0):
            for i in range(10):
                cpx.pixels[i] = (0,0,0)


    #Runtime Exception handler
    except RuntimeError:
        print("Retrying!")

    sleep(0.5)
