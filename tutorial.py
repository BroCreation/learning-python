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

choice = 0

match choice:
	case 0:
		print("CHOICE 0")
	case _:
		print("Default CHOICE")

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

# Dictionary (key - value list)
print("----DICTIONARY----")
heroes = {
	"Superman": "Clark Kent",
	"Batman": "Bruce Wayne"
}

villains = dict([
	("Loki", "Thor's Brother"),
	("Joker", "Bad man")
])

characters = heroes | villains
print(characters)

print(len(heroes))
print(villains["Joker"])
villains["Joker"] = "Evil Man"

print(list(heroes.items()))
print(list(heroes.keys()))
print(list(heroes.values()))

for villain in villains:
	print(villain)

for hero in heroes.values():
	print(hero)

del heroes["Batman"]
print(heroes.pop("Superman"))

d1 = {"name": "Bread", "price": .88}
print('%(name)s costs $%(price).2f' % d1)

# Sets (list of unordered, unique and immutable(can add/remove but no change) stuff)
print("----SETS----")
s1 = set(["Bro", 7, "Creation", 7])
s2 = {"Paul", 7, "Bro"}
s3 = {0, 1, 2, 3, 4, 5}

# l1 = [0, 1, 2, 3, 4, 5]
# print(s1[0]) can't index this list

s1.add(8)
s1.remove(7) # removes element only if it exists otherwise error
s1.discard("Humpty") # discard removes if it exists or not
print(s1)

print(s1 | s2) # s1 |= s2
print(s1.intersection(s2))
print(s1 & s2)
print(s1.symmetric_difference(s2)) # returns set of uncommon elements from both s1, s2 (union remove intersection)
print(s1 - s2) # returns set s1 after removing common elements from s1, s2

print("Random", s3.pop())

for x in s3:
	print(x)

s3.clear()
s4 = frozenset(["can't", "add", "or", "remove", "anything", "also", "nochange"])

# Functions (resuable code)
print("----Functions----")
def get_sum(num1: int = 1, num2: float = 2.5):
	return num1 + num2

def sum_list(nums):
	sum = 0
	for num in nums:
		sum += num
	return sum

print(sum_list({1, 2, 3}))

def any_num_of_args(*args):
	sum = 0
	for arg in args:
		sum += arg
	return sum

print(any_num_of_args(1, 2, 3, 4, 5, 1))

# Complex Functions
def next_2(num):
	return num + 1, num + 2

i1, i2 = next_2(5) # multiple returns
print('Num 1:', i1, 'Num 2:', i2)

# Anonymous Lambda function
def mult_by(num):
	return lambda x: x * num
# [num](int x) {return x*num} in C++
x = mult_by(7)
print(x(10)); print(mult_by(3)(10))

def mult_list(list, func):
	for x in list:
		print(func(x))

mult_by_4 = mult_by(4)
mult_list(list(range(0, 5)), mult_by_4)

power_list = [
	lambda x: x ** 2,
	lambda x: x ** 3,
	lambda x: x ** 4
]

for func in power_list:
	print(func(2), end=" ")

# Map (executes function on a list)
one_to_4 = range(1, 5)
multlists = lambda x, y: x * y
print('\n', list(map(multlists, one_to_4, one_to_4)), sep='')

# Filter (filters list by some condition)
print(list(filter(lambda x: x % 2 == 0, range(1, 11))))

# Reduce (Takes a list and reduces to one value)
list2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(reduce(lambda x, y: x + y, range(1, 10)))
print(reduce(lambda x, y: x + y, list2d))
print(reduce(lambda x, y: x if(x==30) else y, range(1, 20)))

# Exception Handling - Crash Program = Bad
while True:
	try:
		number = int("A")
		div = 1 / 0
	except ValueError:
		print("You didn't enter a number")
	except Exception as e:
		print(f"Error Occured: {e}")
	break