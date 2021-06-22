import time

f = open("lastboot.txt", "w")
f.write("Hello!" + time.ctime())
f.close()

while True:
  print("Heyo! " + time.ctime())
  time.sleep(10)
