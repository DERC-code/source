#! /usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO # (1)

GPIO.setmode(GPIO.BOARD) # (2)
GPIO.setup(16,GPIO.OUT)  # (3)
while True:
    GPIO.output(16,GPIO.HIGH)  # (4)
GPIO.output(16,GPIO.LOW)  # (4)
GPIO.cleanup() # (5)