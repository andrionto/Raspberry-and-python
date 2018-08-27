import os
import RPi.GPIO as GPIO
import time
import datetime
import sys
import urllib
import urllib2
from urllib import urlencode
from yowsup.env import YowsupEnv
from wasend import YowsupSendStack
from wamedia import SendMediaStack

#inisiasi pin
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print "mulai"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#variabel ulang ambil foto
ulang = 1

def credential():
    return "6287771781203", "Ng0378gCG3V8ki1zpI8eHp+oUts="

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
  print "Distance:",distance,"cm"

  if distance<10:
    while ulang<4:
      dt = str(datetime.datetime.now())
      cek = dt[0:4]+dt[5:7]+dt[8:10]+dt[11:13]+dt[14:16]+dt[17:19]+".jpg"
      os.system("fswebcam /home/pi/proyek2/"+cek)
      
      time.sleep(5)
      if os.path.exists("/home/pi/proyek2/"+cek):
          url = 'http://192.168.43.193:81/proyek2/service/service.php'
          encoded = open("/home/pi/proyek2/"+cek, "rb").read().encode("base64")
          data = {'test': encoded, 'nama' : dt[0:4]+dt[5:7]+dt[8:10]+dt[11:13]+dt[14:16]+dt[17:19]}
          encoded_data = urlencode(data)
          website = urllib2.urlopen(url, encoded_data)
          print website.read()
          print "ada pencuri"
          try:
              stack = SendMediaStack(credential(),[([6285238203429,"/home/pi/proyek2/"+cek])])
              stack.start()
          except:
            pass
      else:
          print "no foto"
      ulang = ulang+1
      

GPIO.cleanup()
