import time

f = open("lastboot.txt", "w")
f.write(time.ctime())
f.close()

while True:
  print("Hi! " + time.ctime())
  time.sleep(10)
