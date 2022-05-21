import RPi.GPIO as GPIO
import time
import cv2
import usb_trial
import os
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # set new dimensionns to cam object (not cap)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

i = 1
while True: 
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")
        directory = str((usb_trial.get_mount_points()[0][1]))
        os.chdir(directory)
        ret,frame = cap.read() # return a single frame in variable `frame`
        cv2.imwrite(str(i)+'.png',frame)
        time.sleep(1)
        i+=1



cap.release()

