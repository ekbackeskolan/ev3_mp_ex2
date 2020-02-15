#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()

#Exempel hämtat från 
#https://antonsmindstorms.com/2019/06/15/how-to-run-python-on-an-ev3-brick/

# Clear the display
brick.display.clear()

# Print ``Hello`` near the middle of the screen
brick.display.text("Hello", (60, 50))

# Print ``World`` directly underneath it
brick.display.text("World")

# Show the current voltage
brick.display.text("Voltage is: {}".format(brick.battery.voltage()))

# Wait until a button is pressed
while not brick.buttons():
    wait(10)
