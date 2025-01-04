''' Imports '''
import sys
import math
import random
import threading
import time
from functools import reduce

# This is python program
print('Hello World \'Quote\' ')
print('''"This is a 'direct' speech"''')
name = 'Bro Creation'
print('Hi', name)

v1 = v2 = 10; v3 = (
		20
		+ 10
	)
v4 = 2 \
	** 8
print(v1, v2, v3, v4)

# Casting
print(ord('2'), chr(65), str(55), int(21.21), sep='-')

# Output
print(13, 11, 2006, sep='/')
print("No Newline", end=' ')
print("%04d %s %.2f %c" % (1, "Derek", 23.221123, 'A'))
print("Random", random.randint(1, 101))
print(1/math.inf)
print(math.sin(math.pi/3))

# Control Flow
# Conditions
age = 15
if age > 21:
	print("You can drive a tractor trailer")
elif age >= 16:
	print("You can drive a car")
else:
	print("You can't drive")
# and or not
if age < 5:
	print("Stay Home")
elif age >= 5 and age <=6:
	print("Go to Kindergarten")
elif age > 6 and age <= 17:
	print("Grade %d" % (age - 5))
else:
	print("College")

canVote = True if age>=18 else False
print(canVote)

# While Loops
i = 0
while i < 20:
	if i % 2 == 0:
		print(i)
	elif i == 9:
		break
	else:
		i += 1
		continue
	i += 1

l4 = [1, 2, 5, 6, 8, 9]
i = 0
while i < len(l4):
	print(l4[i])
	i += 1
# Weird way to print but ok.
while len(l4):
	print(l4.pop(0))

lis1 = [10, 12.25, "Tony", "Stark", True]
for x in lis1:
	print(x, ' ', end="")

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in [0, 1, 2]:
  pass

itr = iter(lis1) # takes iterable obj in func iter() and returns something which allows you to iterate over it
print(next(itr))
print(next(itr))
print(list(range(0, 9)))

# Strings and Manipulation
print(r"This will ignore escape characters: \n \t \"")
str3 = "Hello " + "World"
print(len(str3))
print("1st", str3[0], "Last", str3[-1])
print("1st to 3", str3[0:3], "Btw 0:-1 Every 2nd Step", str3[0:-1:2])
str3 = str3.replace("Hello", "Goodbye")
print(str3)
str3 = str3[:8] + "w" + str3[9:]
print(str3)
print("Goodbye" in str3)
print("Hello" not in str3)
print("l index", str3.find("l"))
print("		Trimmed		".strip()) # lstrip, rstrip

# list of strings to string
print(" ".join(["Some", "Words", "Separator"]))
# String to list of strings
print("A string".split(" "))

print("A String".lower())
print("A String".upper())
print("AString123".isalnum())
print("AString".isalpha())
print("123".isdigit())
print(" ".isspace())

int1 = int2 = 5
print('%d + %d = %d' % (int1, int2, int1 + int2))
print(f'{int1} + {int2} = {int1 + int2}')

# Lists (Mutable - Change)
l1 = [1, 2, 3, 4.32, 'Wasy', True]
print("Length", len(l1))
print("1st", l1[0], "Last", l1[-1])

l1[0] = 5
l1[4:6] = ['Wasay', False] # change - excluding l1[6]
l1[2:2] = [30, 40] # insert at l1[2]
l1.insert(1, "TWO")
l2 = l1 + ["Egg", 4]
l2.remove(4.32)
l2.pop(0)
print("l2", l2)

l3 = [[1, 2], [3, 4]]
print('[1][0]', l3[1][0])
print([1, 2] in l3, 3 in l2)
print("Min", min([1, 2, 3]))
print("Min", max([1, 2, 3]))
print("1 to 2:", l1[0:2])
print("Every Other", l1[0:-1:2]) # start:stop:step
print("Correct Every Other", l1[::2]) # nostart, noend, 2 step - mean all with 2 stepping
print("Reverse", l1[::-1]) # -ve step to go reverse and 1 step

# Tuples (Immutable - Unchanging - Faster)
t1 = (15, 14.99, "Bro")
print("1st:", t1[0])
print("Last:", t1[-1])
print("1st to 2:", t1[0:2])
print("Every Other:", t1[0::2])
print("Reverse:", t1[::-1])
