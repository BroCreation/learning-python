import random
import math
import threading
import time
from functools import reduce

with open("Junk Ideas.txt", mode="a", encoding="UTF-8") as my_file:
    my_file.write("Appending this from python")

with open("Junk Ideas.txt", mode="r", encoding="UTF-8") as my_file:
    print(list(filter(lambda x: x.isdigit(), list(my_file.read()))))