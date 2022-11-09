#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_number = str(number)
L_number = new_number[-1]
last_number = int(L_number)
if last_number > 5:
  print(f"Last digit of {number} is {last_number} and is greater than 5")
elif last_number == 0:
  print(f"Last digit of {number} is {last_number} and is 0")
elif 6 > last_number != 0:
  print(f"Last digit of {number} is {last_number} and is less than 6 and not 0")
else:
  print(0)
