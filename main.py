import time

f = open("demofile3.txt", "w")
f.write(time.ctime())
f.close()

while True:
  print("Hi! " + time.ctime())
  time.sleep(10)
