import time

f = open("lastboot.txt", "w")
f.write("Hello!" + time.ctime())
f.close()

while True:
  print("Hi! " + time.ctime())
  time.sleep(10)
