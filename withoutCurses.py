import random, time
import sys

orders = 0
operations = 0

UP = "\x1B[2A"
CLR = "\x1B[0K"
print("\n")  # set up blank lines so cursor moves work
while True:
   orders += random.randrange(1, 3)
   operations += random.randrange(2, 10)

   #print(f"{UP}Orders: {orders}{CLR}\nOperations: {operations}{CLR}")
   sys.stdout.write(f"{UP}Orders: {orders}{CLR}\n")
   sys.stdout.write(f"Operations: {operations}{CLR}\n")
   #sys.stdout.flush()

   time.sleep(random.uniform(0.5, 2))