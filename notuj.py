import requests

url = "http://andrigunawangh.000webhostapp.com/includes/webservice_noperson.php"
r = requests.get(url)
print(r.text)
