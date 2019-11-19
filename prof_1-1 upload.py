import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)


while True:
    i=GPIO.input(11)
    if i == 0:
        print("Not Detected", i)
        GPIO.output(3,0)
    elif i==1:
        print("Detected",i)
        GPIO.output(40,1)
        time.sleep(2)