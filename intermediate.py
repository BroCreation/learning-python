import random
import math
import time
import threading
import re
# import tutorial
# from tutorial import mult_by_4

with open("New File.txt", mode="w", encoding="utf-8") \
  as file:
  file.write('''Someone once said, "Alhamdulilah!"''')

with open("New File.txt", encoding="utf-8") as file:
  str = file.read()

print(str, file.closed)

class Square:
  def __init__(self, w, h):
    self.w = w
    self.h = h

  # Custom Setters & Getters and maybe: "to private attributes"
  @property
  def h(self):
    print("Retrieving the height")
    return self.__h * 2

  @h.setter
  def h(self, value):
    self.__h = value

  @property
  def w(self):
    return (self.__w*3) / 3

  @w.setter
  def w(self, value):
    self.__w = value

  def get_area():
    return self.__w * self.__h

  def __str__(self):
    return f"{self.__w}{self.__h}\n"

  def __gt__(self, Square):
    if(self.__w > Square.w):
          return True
    else:
          return False

s1 = Square(10, 10)
s2 = Square(20, 10)
s1.w = 11
print(s1)
print(s1 > s2)

def execute_thread(i):
  current_time = time.strftime("%H:%M:%S", time.gmtime())
  print(f"{i} thread is asleep at {current_time}sec")
  sleep_time = random.randint(1, 5)
  time.sleep(sleep_time)
  current_time = time.strftime("%H:%M:%S", time.gmtime())
  print(f"{i} thread is awake at {current_time}sec")

for i in range(1, 10):
  # args must be a sequence - to handle multiple arguments passed to target function() we pass a tuple not just a single value. tuple is requires
  thread = threading.Thread(target=execute_thread, args=(i, ))
  thread.start()
  print('Active Thread:', threading.active_count())
  print('Thread Object List:', list(threading.enumerate()))

# Single Main thread - Sequential
# for i in range(0, 5):
#     execute_thread(i)

def func1(x, y):
  print('Return the sum: ')
  time.sleep(random.randint(1, 5))
  print(x + y)

def func2(x, y):
  print('Return the difference: ')
  time.sleep(random.randint(1, 5))
  print(x - y)

def func3(x, y):
  print('Return the product: ')
  time.sleep(random.randint(1, 5))
  print(x * y)

functions = [func1, func2, func3]

for i in range(3):
  thread = threading.Thread(target=functions[i], args=(2, 3))
  thread.start()

# Regex - regular expression to manipulate strings
mystr = "Aboyul Wasay is a boy!"
if re.search("boy", mystr):
  print("BOY")

lis = re.findall("boy", mystr)
for i in lis:
  print(i)

for i in re.finditer("boy.", mystr):
  tup = i.span()
  print(mystr[tup[0]:tup[1]])

# print(tutorial.mult_by_4(2))

def fact(num):
  return num * fact(num-1) if(num > 1) else 1

print(fact(3))