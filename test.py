from yowsup.env import YowsupEnv
from wamedia import SendMediaStack

notujuan = 6281394081303
#foto = "/home/pi/tugasakhir/smile.jpg"
def credential():
    return "6281212410407","LsXtaeomh44Bps/RgZdgU6QVPng="

try:
   stack = SendMediaStack(credential(),[(notujuan,"/home/pi/tugasakhir/smile.jpg")])
   stack.start()
except:
  pass

