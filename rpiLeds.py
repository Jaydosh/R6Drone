import time
import RPi.GPIO as GPIO

#class Leds():

GPIO.setmode(GPIO.BOARD)

    #def __init__ (self):
    #leds from left to right
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT) 
    GPIO.setup(18, GPIO.OUT)

    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(32, GPIO.OUT)
    GPIO.setup(36, GPIO.OUT)



    #def start(self):
    #up
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(32, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(36, GPIO.HIGH)
    time.sleep(0.5)

    #down
    GPIO.output(16, GPIO.LOW)
    GPIO.output(36, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(32, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    time.sleep(0.5)



    #up
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(32, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(36, GPIO.HIGH)
    time.sleep(0.5)

    #down
    GPIO.output(16, GPIO.LOW)
    GPIO.output(36, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(32, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    time.sleep(0.5)



    #up
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(32, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(36, GPIO.HIGH)
    time.sleep(0.5)

    #down
    GPIO.output(16, GPIO.LOW)
    GPIO.output(36, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(32, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    time.sleep(0.5)




    #final up
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(32, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(36, GPIO.HIGH)
