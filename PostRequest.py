import requests
import time
filepath = "/Users/hakonhukkelas/programmering/ntnu/source.txt"
while True:
  f = open(filepath, 'r')
  message = "".join(f.readlines())
  f.close()
  r = requests.post("http://localhost:8888", data=message)
  time.sleep(10)
