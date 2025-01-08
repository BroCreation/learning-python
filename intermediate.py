import random
import math
import time
import threading

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
    # args must be a sequence because it will contain multiple threads(execute_thread) or i running simulatneously.
    thread = threading.Thread(target=execute_thread, args=(i, ))
    thread.start()
    print('Active Thread:', threading.active_count())
    print('Thread Object List:', list(threading.enumerate()))


