import os
import RPi.GPIO as GPIO
import time

#inisiasi pin
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
ulang = 1
print ("mulai")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while 1:
  ulang = 1 
  GPIO.output(TRIG,True)
  time.sleep(0.00001)
  GPIO.output(TRIG,False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()
    
  while GPIO.input(ECHO)==1:
    pulse_end = time.time()
    
  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance = round(distance, 2)
  print ("Distance:",distance,"cm")
  time.sleep(0.5)

GPIO.cleanup()