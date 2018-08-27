import urllib
import urllib2
from urllib import urlencode

url = 'http://192.168.43.193:81/service/service.php'
encoded = open("20170113102232.jpg", "rb").read().encode("base64")

data = {'test': encoded, 'nama' : '20170113102232'}
encoded_data = urlencode(data)

website = urllib2.urlopen(url, encoded_data)
print website.read()

